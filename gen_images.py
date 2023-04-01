import requests
from dotenv import load_dotenv
import os
import openai

def gen(prompt_list):
    load_dotenv()

    # Set up the OpenAI API client
    openai.api_key = os.getenv("OPENAI_API_KEY")

    # Set up the image prompt
    prompt = 'Retelling of Rasputins death attempt - poison, bullets, and drowning.'
    prompt_2 = 'The rapper Ice Spice giving a presentation to a high school class'

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
        with open('generated_image_{}.jpg'.format(num), 'wb') as f:
            f.write(response.content)

        num+=1

