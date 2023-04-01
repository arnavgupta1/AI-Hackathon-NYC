import gen_script
import gen_audio
import gen_images
import topic_to_wikiurl

CHARACTERS = {
        "icespice": "You will be presenting the information like the rapper Ice Spice. She likes to call people munches."
}

DEFAULT_CHARACTER = "icespice"
DEFAULT_TOPIC = "Rasputin"
DEFAULT_SOURCE = "https://en.wikipedia.org/wiki/Grigori_Rasputin"

if __name__ == "__main__":
    # get user input for topic
    user_topic = input("Enter a topic: ")

    # get source for the user-provided topic
    wiki_page = topic_to_wikiurl.get_wikipedia_page(user_topic)
    if wiki_page:
        topic = user_topic
        source = wiki_page
    else:
        topic = DEFAULT_TOPIC
        source = DEFAULT_SOURCE
        print("No matching Wikipedia page found, defaulting to " + topic)

    # get user input for character
    print("These are the available voices: " + ', '.join(list(CHARACTERS.keys())))
    character = input("Enter a character: ")
    if character not in list(CHARACTERS.keys()):
        print(character + " is not available, defaulting to " + DEFAULT_CHARACTER)
        character = DEFAULT_CHARACTER

    # generate the transcript and timestamped image descriptions
    print("generating script...")
    [transcript, image_prompts] = gen_script.gen(character, topic, source) #outputted as lists

    # generate audio for the transcript
    print("generating audio...")
    audio_list = []
    for transcript_output in transcript:
        #Stores all audio files in a list
        audio_list.append(gen_audio.gen(transcript_output, 'output.mp3'))  

    # generate images for the video
    print("generating images...")
    gen_images.gen(topic, image_prompts)

    # generate video by combining images, video, and audio
    # TODO

