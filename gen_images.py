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
    gen("Rasputin", ['[Image 1 prompt: Fish swimming in clear ocean water, showcasing their diversity.]', '[Image 2 prompt: A variety of colorful fish showing their different shapes and sizes.]', '[Image 3 prompt: Evolution of fish from ancient fossils to present-day species.]', '[Image 4 prompt: Close-up of fish gills, fins, and scales, with an anglerfish displaying its luminescent feature.]', '[Image 5 prompt: Vibrant coral reef with a diverse array of fish coexisting, juxtaposed with damaged reef affected by overfishing and climate change.]', '[Image 6 prompt: A diverse group of fish swimming together, symbolizing unity and coexistence among species.]'])
