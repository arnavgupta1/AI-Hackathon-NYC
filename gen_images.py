import requests
from dotenv import load_dotenv
import os
import openai

def gen(topic, prompt_list):
    load_dotenv()

    # Set up the OpenAI API client
    openai.api_key = os.getenv("OPENAI_API_KEY")

    if not os.path.exists(topic):
        os.mkdir(topic)
        print(f"Directory {topic} created")
    else:
        print(f"Directory {topic} already exists")

    num = 1
    for prompt_element in prompt_list:
        # Generate the image using the prompt
        response = openai.Image.create(prompt=prompt_element)
        print(response)
        # Get the URL of the generated image
        url = response.data[0].url

        # Download the image
        response = requests.get(url)

        # Save the image to a file
        img_path = '{}/image{}.jpg'.format(topic, num)
        if not os.path.exists(img_path):
            with open(img_path, 'wb') as f:
                f.write(response.content)
        else:
            print(f'{img_path} already exists \n Skipping ......')

        num+=1

# for quick testing out of pipeline
if __name__ == "__main__":
    print("testing image generation")
    gen("Emu War",['Image 1: A group of emus in a Western Australian wheat field', 'Image 3: Australian military personnel preparing for the Emu War', 'Image 4: Soldiers positioning their Lewis machine guns', 'Image 6: Frustrated soldiers reloading their weapons', 'Image 7: Emus triumphantly wandering the farmlands after evading gunfire', 'Image 9: Headlines about the military defeat against emus in Australian newspapers', 'Image 10: Emu War commemorative artwork, showing soldiers and emus in conflict', 'Image 12: A plaque or historical marker detailing the Emu War and its significance in Australian history'])
