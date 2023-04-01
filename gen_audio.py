import requests
import os
from dotenv import load_dotenv

def gen(transcript, output_file):
    load_dotenv()

    # Replace these values with your own
    api_key = os.getenv("ELEVENLABS_API_KEY")
    voice_id = os.getenv("ELEVENLABS_VOICE_ID")

    # API endpoint and headers
    url = f'https://api.elevenlabs.io/v1/text-to-speech/{voice_id}'
    headers = {
        'xi-api-key': api_key,  # Update the header to use xi-api-key
        'Content-Type': 'application/json'
    }

    # Request payload
    payload = {
        'text': transcript,
        'voice_settings': {
            'stability': 0,
            'similarity_boost': 0
        }
    }

    # Make the API call
    response = requests.post(url, headers=headers, json=payload)

    # Check the response
    if response.status_code == 200:
        # Save the audio file
        with open(output_file, 'wb') as audio_file:
            audio_file.write(response.content)
        print('Audio file saved as ' + output_file)
    else:
        print(f'Error: {response.status_code} - {response.content.decode("utf-8")}')

