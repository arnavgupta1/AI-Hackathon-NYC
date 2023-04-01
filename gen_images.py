import requests
from dotenv import load_dotenv
import os
import openai

def gen(topic, prompt_list):
    load_dotenv()

    # Set up the OpenAI API client
    openai.api_key = os.getenv("OPENAI_API_KEY")

    num = 1

    # TODO : Check for directory before creating it
    os.mkdir(topic)
    for prompt_element in prompt_list:
        # Generate the image using the prompt
        response = openai.Image.create(prompt=prompt_element)
        print(response)
        # Get the URL of the generated image
        url = response.data[0].url

        # Download the image
        response = requests.get(url)

        # Save the image to a file

        #TODO : Check for image with same name before creating it
        with open('{}/generated_image_{}.jpg'.format(topic, num), 'wb') as f:
            f.write(response.content)

        num+=1

