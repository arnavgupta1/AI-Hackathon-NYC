import requests

# Replace these values with your own
api_key = '6778716bd3b83651ee01f53c88a265e1'
voice_id = 'dwdRJnffs5XslqI4IhLx'
text = 'Hello everyone!'

# API endpoint and headers
url = f'https://api.elevenlabs.io/v1/text-to-speech/{voice_id}'
headers = {
    'xi-api-key': api_key,  # Update the header to use xi-api-key
    'Content-Type': 'application/json'
}

# Request payload
payload = {
    'text': text,
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
    with open('output_audio.mp3', 'wb') as audio_file:
        audio_file.write(response.content)
    print('Audio file saved as output_audio.mp3')
else:
    print(f'Error: {response.status_code} - {response.content.decode("utf-8")}')
