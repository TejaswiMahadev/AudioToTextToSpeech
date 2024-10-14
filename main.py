import yt_dlp
import uuid
import asyncio
import os
from deepgram import Deepgram
import streamlit as st
from elevenlabs import ElevenLabs, Voice, VoiceSettings

# Deepgram and ElevenLabs API keys
DEEPGRAM_API_KEY = '8ac6425116a55329e03025d0dcdd9ba65978d522'
ELEVENLABS_API_KEY = 'sk_8454fed99afd701bb6d871a280aac5150e7cb8d0abd97403'

def download_audio_from_youtube(url):
    unique_filename = f"audio_{uuid.uuid4()}.mp3"
    ydl_opts = {
        'format': 'bestaudio[ext=m4a]/bestaudio/best',
        'outtmpl': unique_filename,
        'verbose': True,
        'postprocessors': []  # No FFmpeg required
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    if not os.path.exists(unique_filename):
        raise FileNotFoundError(f"Downloaded audio file '{unique_filename}' not found.")

    return unique_filename

async def transcribe_audio_deepgram(audio_file, deepgram_api_key):
    deepgram = Deepgram(deepgram_api_key)

    with open(audio_file, 'rb') as audio:
        source = {'buffer': audio, 'mimetype': 'audio/mp3'}
        response = await deepgram.transcription.prerecorded(source, {'punctuate': True})
        transcript = response['results']['channels'][0]['alternatives'][0]['transcript']
    
    return transcript

def convert_text_to_audio_elevenlabs(transcript, output_audio='output_audio.mp3'):
    client = ElevenLabs(api_key=ELEVENLABS_API_KEY)

    voice = Voice(
        voice_id="ZQe5CZNOzWyzPSCn5a3c",
        settings=VoiceSettings(
            stability=0,
            similarity_boost=0.75
        )
    )

    audio_generator = client.generate(
        text=transcript,
        voice=voice
    )

    audio_bytes = b"".join(audio_generator)
    with open(output_audio, 'wb') as f:
        f.write(audio_bytes)

    return output_audio

# Streamlit UI
def main():
    st.title("YouTube Audio Transcription and Text-to-Speech")

    youtube_url = st.text_input("Enter YouTube URL")

    if st.button("Process"):
        if youtube_url:
            with st.spinner("Downloading audio..."):
                try:
                    audio_file_path = download_audio_from_youtube(youtube_url)
                    st.success("Audio downloaded successfully.")
                except Exception as e:
                    st.error(f"Error downloading audio: {e}")
                    return

            with st.spinner("Transcribing audio..."):
                try:
                    transcript = asyncio.run(transcribe_audio_deepgram(audio_file_path, DEEPGRAM_API_KEY))
                    st.success("Transcription complete.")
                    st.text_area("Transcript", transcript, height=200)
                except Exception as e:
                    st.error(f"Error during transcription: {e}")
                    return

            with st.spinner("Converting transcript to speech..."):
                try:
                    output_audio_path = convert_text_to_audio_elevenlabs(transcript)
                    st.success("Text-to-speech conversion complete.")

                    st.audio(output_audio_path)

                    with open(output_audio_path, 'rb') as f:
                        st.download_button(label="Download Generated Audio", data=f, file_name=output_audio_path, mime='audio/mp3')

                except Exception as e:
                    st.error(f"Error during text-to-speech conversion: {e}")
        else:
            st.error("Please provide a valid YouTube URL.")

if __name__ == "__main__":
    main()

