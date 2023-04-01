import os
from dotenv import load_dotenv
import openai

load_dotenv()

openai.organization = "org-9gFweLPBiQroCILySsu6cZBQ"
openai.api_key = os.getenv("OPENAI_API_KEY")

roles = {
        "base": "Your job is to act like a college professor, accurately and concisely summarizing source information. You will be given one minute and 30 seconds to make a youtube short type of content. Mention any shocking or usual content. Avoid lengthy exposition and give more stories. Please provide an uninterrupted transcript without any cues like (enthusiastically). Anything you say should only be found in the transcript. After the transcript provide images/graphics/animations you want playing in the background and their time stamps. Label the transcript like this: ::transcript:: and the images/graphics/animations like this ::timestamps:: \n [00:00-00:20] description \n [00:21-00:52] description",
    "icespice": "You are to act as Ice Spice. Ice Spice calls people munches."
}

user_input = "Your topic is: Rasputin. Your source material is: (https://en.wikipedia.org/wiki/Grigori_Rasputin)"

MODEL='gpt-4'

completion = openai.ChatCompletion.create(
  model=MODEL,
  max_tokens=1200,
  messages=[
    {"role": "system", "content": roles["base"]},
    {"role": "system", "content": roles["icespice"]},
    {"role": "user", "content": user_input}
  ]
)

print(completion)
