import os
from dotenv import load_dotenv
import json
import openai

def gen():
    load_dotenv()

    openai.organization = "org-9gFweLPBiQroCILySsu6cZBQ"
    openai.api_key = os.getenv("OPENAI_API_KEY")

    character = {
            "base": "Your job is to act like a college professor, accurately and concisely summarizing source information. You will be given one minute and 30 seconds to make a youtube short type of content. Mention any shocking or usual content. Avoid lengthy exposition and give more stories. Please provide an uninterrupted transcript without any cues like (enthusiastically). Anything you say should only be found in the transcript. After the transcript provide a description of the images you want playing in the background and their time stamps. Label the list of timestamped image descriptions like this: \n\n ::timestamps:: \n [00:00-00:20] description \n [00:21-00:52] description",
        "icespice": "You are to act as Ice Spice. Ice Spice calls people munches."
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


