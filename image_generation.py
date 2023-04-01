import requests
from dotenv import load_dotenv
import os
import openai

def image_gen():
    load_dotenv()

    # Set up the OpenAI API client
    openai.api_key = os.getenv("OPENAI_API_KEY")

    # Set up the image prompt
    prompt = 'Retelling of Rasputins death attempt - poison, bullets, and drowning.'
    prompt_2 = 'The rapper Ice Spice giving a presentation to a high school class'

    prompt_list = [
        'A hand-drawn animated portrait of Grigori Rasputin with his iconic beard and intense eyes.',
        'A scene depicting Rasputin healing young Alexei while Tsar Nicholas II and Alexandra watch anxiously.',
        'A montage of Rasputins controversial behavior, including him flirting with women and drinking heavily in a dimly lit bar.',
        'A dramatic animation of the assassination attempt, showing Rasputin being offered poisoned wine and pastries, being shot multiple times, and being thrown into the icy Neva River.',
        'A somber image of the frozen Neva River with the text "The End of Rasputin" appearing on the screen.'
    ]

    num = 3
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

        num += 1

