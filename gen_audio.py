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
    gen("Rasputin", "21m00Tcm4TlvDq8ikWAM",["Gather 'round, munches, and let me tell ya about Rasputin, a Russian mystic and spiritual healer who rose to fame in the early 20th century! Born in Siberia, this mysterious man had an uncanny ability to influence the powerful Romanov family, Russia's last royal dynasty.", "Now, let me tell you how Rasputin got into the inner circles of one of the most famous royal families. Tsar Nicholas II and Alexandra, his wife, had a son named Alexei, who suffered from hemophilia. Nothin' seemed to help the poor boy until Rasputin came along. With his mystical powers and prayers, he appeared to control the boy's bleeding episodes, and that's how he gained the royals' trust.", "Rasputin's influence, though, extended beyond just healin' the young prince. He got real cozy with the Russian royals, providing them with advice on various matters, munches. That ruffled some feathers among the nobility and the church – no one could believe that a simple Siberian could have that much sway over the Tsar!", "Despite his closeness to the royal family, our man Rasputin wasn't all sunshine and rainbows. He had quite a reputation for his hedonistic lifestyle, includin' drinkin', partyin', and escapades with the ladies. And guess what, munches, talk like that about Rasputin stoked hatred among church authorities and nobles, who sought to dethrone him.", "Now, here's where things get juicy – in December 1916, a group of haters, includin' Prince Felix Yusupov, Grand Duke Dmitri Pavlovich, and some other confidantes, plotted to assassinate Rasputin. They invited him to Yusupov Palace, but what Big R didn't know was that this party was gonna be his last!", "These plotters ain't no amateurs, munches. They poisoned Rasputin with cyanide-laced wine and cakes. But here's the shocker – Rasputin didn't keel over! That's when they shot him, but still, he managed to escape! Finally, after a dramatic chase, they shot him twice more and even bashed his head in. Phew, our man had some serious stamina!", "But this ain't just a wild assassination story, munches. The fall of Rasputin also has implications for Russia. After his demise, those intense rumors around his influence on the royal family led to a loss of trust in the Romanov Dynasty, eventually contributin' to the 1917 Russian Revolution and the family's brutal end. Razzy's story truly is a cautionary tale, y'all!"])
