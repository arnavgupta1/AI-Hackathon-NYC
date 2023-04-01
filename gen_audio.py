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

    n=0
    for transcript_output in transcript:
        # Request payload
        payload = {
            'text': transcript_output,
            'voice_settings': {
                'stability': .25,
                'similarity_boost': .95
            }
        }

        # Make the API call
        response = requests.post(url, headers=headers, json=payload)

        # Check the response
        if response.status_code == 200:
            # Save the audio file
            output_path = '{}/audio{}.mp3'.format(topic, n)
            if not os.path.exists(output_path):
                with open(output_path, 'wb') as f:
                    f.write(response.content)
                    print('Audio file saved as ' + output_path )
            else:
                print(f'{output_path} already exists \n Skipping ......')
        else:
            print(f'Error: {response.status_code} - {response.content.decode("utf-8")}')
        n+=1

# for quick testing out of pipeline
if __name__ == "__main__":
    print("testing audio generation")
    gen("Rasputin", "WqKktePcV6Na82uGScz8", ["Yo munches, gather 'round, let's talk about Rasputin, a Russian mystic who rose to fame in the early 20th century. Born into a peasant family, this dude had a strong religious calling, and some mysterious healing powers."])


