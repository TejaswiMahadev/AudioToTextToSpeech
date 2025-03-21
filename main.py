import yt_dlp
import uuid
import asyncio
import os
from deepgram import Deepgram
import streamlit as st
from elevenlabs import ElevenLabs, Voice, VoiceSettings

# Deepgram and ElevenLabs API keys
DEEPGRAM_API_KEY = 'YOUR_DEEPGRAM_API_KEY'
ELEVENLABS_API_KEY = 'YOUR_ELEVENLABS_API_KEY'

def download_audio_from_youtube(url):
    unique_filename = f"audio_{uuid.uuid4()}.mp3"
    
    # Create a temporary cookies file with required YouTube cookies
    cookie_data = """# Netscape HTTP Cookie File
# https://curl.haxx.se/rfc/cookie_spec.html
# This is a generated file!  Do not edit.

.youtube.com	TRUE	/	FALSE	1735376022	ST-3opvp5	session_logininfo=AFmmF2swRQIgA_8mSC84hj5feCdS_9PItz2xg3KjngZIItmnXr-Kg5MCIQC769yAStIBeMiNNsquMwjmRzm8WMhl47sgL6UaM-0yzw%3AQUQ3MjNmeHFZUnBMNGNGaDdsZkJDYkFXWTRmSUhYS1Q5TTdBbjdGZlRRV05GLW1SNWo5Mm9jLUhoaEg0ejFyTVNiajhOZEpJQ2FnUTFQV0VDMUpHM19QSjA0LXVfQjJYUXNYNlVxdkdGM1AzMlNNNVVxX2tjNDRHUGlDV3F2ZXR3MFpGQmF4ZTVBMWtpV1JtaXMxYnNoczRVT3hnWU1icjlR
.youtube.com	TRUE	/	TRUE	1768224454	__Secure-3PSID	g.a000rAggHCjGE0ihtH7UiCDBLeqlhKuLdm4X5SbAe4baDM-9BJ68DAN_ObrD2NdMhCXBfeH6xAACgYKAfASARcSFQHGX2Miwc303xsYD3SZXp3bcxAb2RoVAUF8yKrzWJBVKNqVByn6gViRXODl0076
.youtube.com	TRUE	/	FALSE	1766912019	SIDCC	AKEyXzVsHNtXNSb8GX5cujqFe4L-E8m5ewzvnAmDALNld7P11xCd0dEIC5X4PES23qhEwEvOcw
.youtube.com	TRUE	/	FALSE	1768224454	SID	g.a000rAggHCjGE0ihtH7UiCDBLeqlhKuLdm4X5SbAe4baDM-9BJ68w8imf8gOkaleJDNctkrIggACgYKAT0SARcSFQHGX2Mi5TO4p8tjg7IHgjRU9DgHtxoVAUF8yKqOmEHqihs9TTMBHYRQcoVU0076
.youtube.com	TRUE	/	TRUE	1766910129	__Secure-1PSIDTS	sidts-CjIB7wV3sUHS-PvMIjVo4rQiTXwW1rEeBBLOczdFcQpCblw7qK7ioLF5cPo7BeIf_yamwRAA
.youtube.com	TRUE	/	TRUE	1768224454	SAPISID	rz_UdGn_ztvaXJgj/Ayj6VPsyUBi_vriBw
.youtube.com	TRUE	/	TRUE	1766912019	__Secure-1PSIDCC	AKEyXzWHS-XGlF9EYLU0gvtFqSdbU4GPaFDXh5JiT-23AC7PmRJnUPPZpzWf9qnqhclr3qDllQ
.youtube.com	TRUE	/	TRUE	1768224454	SSID	AI8oNeiQFH8T98KRM
.youtube.com	TRUE	/	TRUE	1768224454	__Secure-1PAPISID	rz_UdGn_ztvaXJgj/Ayj6VPsyUBi_vriBw
.youtube.com	TRUE	/	TRUE	1768224454	__Secure-1PSID	g.a000rAggHCjGE0ihtH7UiCDBLeqlhKuLdm4X5SbAe4baDM-9BJ68kLdJqszBRyUy5CG56JmOswACgYKAYkSARcSFQHGX2MiGoB2-IbfuXmqwyCfgzzYKhoVAUF8yKqRegmnuZnutdxAsN2kIIdO0076
.youtube.com	TRUE	/	TRUE	1768224454	__Secure-3PAPISID	rz_UdGn_ztvaXJgj/Ayj6VPsyUBi_vriBw
.youtube.com	TRUE	/	TRUE	1766912019	__Secure-3PSIDCC	AKEyXzVcD8r1dk2yCgh6MERm-VB-viXnFmQrmxu623NNaYf1JQ1oT29wBfwfQF_iHD1l78EDAyk
.youtube.com	TRUE	/	TRUE	1766910129	__Secure-3PSIDTS	sidts-CjIB7wV3sUHS-PvMIjVo4rQiTXwW1rEeBBLOczdFcQpCblw7qK7ioLF5cPo7BeIf_yamwRAA
.youtube.com	TRUE	/	FALSE	1768224454	APISID	ksAJ2KR64FWdAQFT/Ap6fpO1KVTEQPhZtd
.youtube.com	TRUE	/	FALSE	1768224454	HSID	Adg09krWduHyCSxsq
.youtube.com	TRUE	/	TRUE	1764248810	LOGIN_INFO	AFmmF2swRQIgA_8mSC84hj5feCdS_9PItz2xg3KjngZIItmnXr-Kg5MCIQC769yAStIBeMiNNsquMwjmRzm8WMhl47sgL6UaM-0yzw:QUQ3MjNmeHFZUnBMNGNGaDdsZkJDYkFXWTRmSUhYS1Q5TTdBbjdGZlRRV05GLW1SNWo5Mm9jLUhoaEg0ejFyTVNiajhOZEpJQ2FnUTFQV0VDMUpHM19QSjA0LXVfQjJYUXNYNlVxdkdGM1AzMlNNNVVxX2tjNDRHUGlDV3F2ZXR3MFpGQmF4ZTVBMWtpV1JtaXMxYnNoczRVT3hnWU1icjlR
.youtube.com	TRUE	/	TRUE	1769932983	PREF	tz=Asia.Calcutta&f4=4000000&f6=40000000&f7=10100&f5=20000
www.youtube.com	FALSE	/	FALSE	1769936003	QUESTION_AI_PCUID	78ruc1dqtmuypcgo76wy2crdlzc90d_1732020108"""

    cookie_file = "youtube_cookies.txt"
    with open(cookie_file, "w", encoding='utf-8') as f:
        f.write(cookie_data)
    
    ydl_opts = {
        'format': 'bestaudio[ext=m4a]',
        'outtmpl': unique_filename,
        'cookiefile': cookie_file,
        'verbose': True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
        }],
        'socket_timeout': 30,
        'retries': 10,
        'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
    except Exception as e:
        # If first attempt fails, try with minimal options
        minimal_opts = {
            'format': 'bestaudio',
            'outtmpl': unique_filename,
            'cookiefile': cookie_file,
            'quiet': False
        }
        with yt_dlp.YoutubeDL(minimal_opts) as ydl:
            ydl.download([url])
    
    # Clean up cookie file
    try:
        os.remove(cookie_file)
    except:
        pass
        
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

