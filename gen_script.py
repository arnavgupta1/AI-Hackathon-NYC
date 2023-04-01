import os
from dotenv import load_dotenv
import json
import openai
import textwrap


def gen(character, topic, source):
    load_dotenv()

    openai.organization = "org-9gFweLPBiQroCILySsu6cZBQ"
    openai.api_key = os.getenv("OPENAI_API_KEY")

    SYSTEM_CHARACTER_BASE = "Your job is to act like a college professor, accurately and concisely summarizing source information. You will be given 1000 characters towards generating a transcript for the information. The transcript should not include anything besides the exact words she would want spoken. This includes any expressions, exposition, or images. Mention any shocking or usual content. Avoid lengthy exposition and provide interesting stories. The transcript should have ten parts in broke up in the following format: \nDescription of the material.\nImage: Description of an image related to the material.\n\nProvide specific and high quality image prompts for Dalle 2. All images should have a similar style and should not include any text. Do not include any other labels. Do not number the images."

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
    c = completion.choices[0].message.content.split('Image:')
    print(c)

    transcript = c[::2]
    image_prompts = c[1::2]

    print(transcript)
    print(image_prompts)

    return [transcript, image_prompts]

# for quick testing out of pipeline
if __name__ == "__main__":
    print("testing script generation")
    gen("You will be presenting the information like the rapper Ice Spice. She likes to call people munches.", "Rasputin", "https://en.wikipedia.org/wiki/Grigori_Rasputin")
