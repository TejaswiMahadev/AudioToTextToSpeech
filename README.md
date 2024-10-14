# AudioToTextToSpeech

# YouTube Audio Transcription and Text-to-Speech

This Streamlit application allows users to transcribe audio from YouTube videos and convert the transcript into speech using ElevenLabs' Text-to-Speech (TTS) API.

## Features
- Download audio from a specified YouTube video URL.
- Transcribe the downloaded audio using Deepgram's transcription API.
- Convert the transcript into speech using ElevenLabs' TTS API.
- Render the generated audio in the app for playback.
- Provide an option to download the generated audio.

## Prerequisites

- Python 3.7 or higher
- YouTube video URL for audio transcription
- API Key Retrieval
   ##Deepgram API Key
      1. Sign Up for an Account:
         - Go to the Deepgram website.
         - Click on the "Get Started" button and create a free account by providing your email and password.
      2. Verify Your Email:
         - Check your email for a verification link from Deepgram. Click the link to verify your account.
      3. Access the Dashboard:
         - After verification, log in to your Deepgram account.
         - Navigate to the API Keys section on your dashboard.
      4. Create a New API Key:
         - Click on the "Create API Key" button.
         - Name your API key (e.g., "Streamlit App Key") and select the necessary permissions.
         - Click "Create" to generate your API key.
      5. Copy the API Key:
         - Once created, copy the API key. You'll need to replace the placeholder in the code with this key.
   ##ElevenLabs API Key
      1. Sign Up for an Account:
         - Visit the ElevenLabs website.
         - Click on "Sign Up" and provide the required information to create a new account.
      2. Verify Your Email:
         - Check your inbox for a verification email and click on the verification link to activate your account.
      3. Access the Dashboard:
         - After activation, log in to your ElevenLabs account.
         - Go to the API Keys section in your account settings.
      4. Create a New API Key:
         - Click on the "Create API Key" button.
         - Name your API key (e.g., "Streamlit App Key") and set any restrictions if necessary.
         - Click "Generate" to create the API key.
      5. Copy the API Key:
         - Once generated, copy the API key. Make sure to keep it secure and do not share it publicly

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/AudioToTextToSpeech.git
   cd AudioToTextToSpeech
