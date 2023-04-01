import requests
import os
from dotenv import load_dotenv

def gen(topic, voice_id, transcript):
    load_dotenv()

    # audio generation api
    api_key = os.getenv("ELEVENLABS_API_KEY")

    # API endpoint and headers
    url = f'https://api.elevenlabs.io/v1/text-to-speech/{voice_id}'
    headers = {
        'xi-api-key': api_key,  # Update the header to use xi-api-key
        'Content-Type': 'application/json'
    }

    # Create output file
    if not os.path.exists(topic):
        os.mkdir(topic)
        print(f"Directory {topic} created")
    else:
        print(f"Directory {topic} already exists")
        return

    n=0
    for transcript_output in transcript:
        # Request payload
        payload = {
            'text': transcript_output,
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
            output_path = '{}/audio{}.jpg'.format(topic, num)
            if not os.path.exists(img_path):
                with open(output_file, 'wb') as f:
                    f.write(response.content)
                    print('Audio file saved as ' + output_file)
            else:
                print(f'{output_path} already exists \n Skipping ......')
        else:
            print(f'Error: {response.status_code} - {response.content.decode("utf-8")}')
        n+=1


