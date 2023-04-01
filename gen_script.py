import os
import re
from dotenv import load_dotenv
import json
import openai
import textwrap


def gen(character, topic, source):
    load_dotenv()

    openai.organization = "org-9gFweLPBiQroCILySsu6cZBQ"
    openai.api_key = os.getenv("OPENAI_API_KEY")

    SYSTEM_CHARACTER_BASE = """Your job is to act like a college professor, accurately and concisely summarizing source information. Generate a transcript approximately 600 words long. Mention any shocking or usual content. Avoid lengthy exposition and provide interesting stories. The transcript should have at least eight parts broken up in the following format: 

Text: Description of the material.
Image: Description of an image related to the material.

Provide specific and high-quality image prompts for Dalle 2. All images should have a similar style and should not include any text. Follow the format exactly. Do not number the sections."""

    user_input = "Your topic is: " + topic + "\nYour source material is: " + source

    # gpt-3.5-turbo	gpt-4

    MODEL='gpt-4'

    # Get the full transcript
    completion = openai.ChatCompletion.create(
      model=MODEL,
      max_tokens=1200,
      messages=[
        {"role": "system", "content": SYSTEM_CHARACTER_BASE},
        {"role": "system", "content": character},
        {"role": "user", "content": user_input}
      ]
    )
    c = completion.choices[0].message.content
    # try to remove any numberings but leave dates alone
    c = re.sub(r'(?<!\d)\d{1,2}\.(?!\d)', '', c)
    # seperate transcript from image prompts

    text = []
    images = []

    components = c.split('\n')

    print(components)

    for component in components:
        if component.startswith('Text:'):
            text.append(component[len('Text:'):].strip())
        elif component.startswith('Image:'):
            images.append(component[len('Image:'):].strip())

    print(text)
    print(images)

    return [text, images]

# for quick testing out of pipeline
if __name__ == "__main__":
    print("testing script generation")
    gen("You will be presenting the information like the rapper Ice Spice. She likes to call people munches.", "Rasputin", "https://en.wikipedia.org/wiki/Grigori_Rasputin")
