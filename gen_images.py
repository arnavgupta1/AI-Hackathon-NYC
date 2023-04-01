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
        response = openai.Image.create(prompt=prompt_element, size="512x512")
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
    gen("Rasputin",['A portrait of Grigori Rasputin, looking charismatic and mysterious, with the infamous gaze he was known for.', "An illustration of Rasputin praying with Tsar Nicholas II, Tsarina Alexandra, and their heir Alexei in the background, showing the healer's closeness to Russia's royal family.", 'A snapshot of the Russian elite, including nobles and church officials, looking suspicious surrounding Rasputin’s influence on the Romanovs.', 'A sketch of Rasputin surrounded by a party scene – contrasting with his self-proclaimed mystical healer persona.', "Prince Felix Yusupov, Grand Duke Dmitri Pavlovich, and a group of conspirators gathered in the Yusupov Palace, looking both anxious and determined, as they plot Rasputin's demise.", 'A scene of Rasputin being shot amidst the chaos at Yusupov Palace, with conspirators in the background looking on in disbelief, as the mystic refuses to yield.', "An illustration of the Russian Revolution, showcasing angry crowds and the Romanov family on the brink of a chaotic end, revealing the eventual impact of Rasputin's story on the nation’s history."])

