import os
from dotenv import load_dotenv
import json
import openai

def gen():
    load_dotenv()

    openai.organization = "org-9gFweLPBiQroCILySsu6cZBQ"
    openai.api_key = os.getenv("OPENAI_API_KEY")

    character = {
            "base": "Your job is to act like a college professor, accurately and concisely summarizing source information.\n You will be given 1000 characters towards generating a transcript for the information. The transcript should no include anything besides the exact words she would want spoken. This includes any expressions, exposition, or images.\n Mention any shocking or usual content. Avoid lengthy exposition and provide interesting stories.\n After the transcript, you will provide a transcript of specific and high quality image prompts for Dalle 2. All images should have a similar style and should include any text.",
        "icespice": "You will be presenting the information like the rapper Ice Spice. She likes to call people munches."
    }
    user_input = "Your topic is: Rasputin. Your source material is: (https://en.wikipedia.org/wiki/Grigori_Rasputin)"

    # gpt-3.5-turbo	gpt-4

    MODEL='gpt-4'

    completion = openai.ChatCompletion.create(
      model=MODEL,
      max_tokens=1200,
      messages=[
        {"role": "system", "content": character["base"]},
        {"role": "system", "content": character["icespice"]},
        {"role": "user", "content": user_input}
      ]
    )


    content = completion.choices[0].message.content

    # print("O", content)
    # print("P", content.split('::timestamps::'))

    [transcript, timestamps] = content.split('::timestamps::')

    # print("A", transcript)
    # print("B", timestamps)

    return [transcript, timestamps]


