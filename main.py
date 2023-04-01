import gen_script
import gen_audio
import gen_images
import topic_to_wikiurl

CHARACTERS = {
        "icespice": {
            "image": "IceSpice.jpeg",
            "prompt": "You will be presenting the information like the rapper Ice Spice. She likes to call people munches.",
            "voiceid": "21m00Tcm4TlvDq8ikWAM"
            },
        "obama": {
            "image": "BarackObama.jpeg",
            "prompt": "You will be presenting the information like the rapper Ice Spice. She likes to call people munches.",
            "voiceid": "WqKktePcV6Na82uGScz8"
            },
        "goggins": {
            "image": "DavidGoggins.jpeg",
            "prompt": "You will be presenting the information like the rapper Ice Spice. She likes to call people munches.",
            "voiceid": "ArcoL01cikeumeyvjemL"
            },
        "rogan": {
            "image": "JoeRogan.jpeg",
            "prompt": "You will be presenting the information like the rapper Ice Spice. She likes to call people munches.",
            "voiceid": "f0Z5Y9B7vR9u1LhfL0ez"
            },
        "popsmoke": {
            "image": "PopSmoke.jpeg",
            "prompt": "You will be presenting the information like the rapper Ice Spice. She likes to call people munches.",
            "voiceid": "94WLagzOB7RS6D80oAiE"
            },
        "shapiro": {
            "image": "BenShapiro.jpeg",
            "prompt": "You will be presenting the information like the rapper Ice Spice. She likes to call people munches.",
            "voiceid": "ySNPIsRlbE2yrsNExgD2"
            },
        "trump": {
            "image": "DonaldTrump.jpeg",
            "prompt": "You will be presenting the information like the rapper Ice Spice. She likes to call people munches.",
            "voiceid": "260YmWEDlmikdW3yL0AD"
            },
        "biden": {
            "image": "JoeBiden.jpeg",
            "prompt": "You will be presenting the information like the rapper Ice Spice. She likes to call people munches.",
            "voiceid": "cZSio7pCP0GQIc32hzFy"
            },
        "lebron": {
            "image": "LebronJames.jpeg",
            "prompt": "You will be presenting the information like the rapper Ice Spice. She likes to call people munches.",
            "voiceid": "ZUyNgkCzbrIucBtAWTLk"
            },
        "queenlizzy": {
            "image": "QueenLizzy.jpeg",
            "prompt": "You will be presenting the information like the rapper Ice Spice. She likes to call people munches.",
            "voiceid": "FAy1wc7Amqw8gkucnrhI"
            }
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
    [transcript, image_prompts] = gen_script.gen(CHARACTERS[character]["prompt"], topic, source) #outputted as lists

    # generate audio for the transcript
    print("generating audio...")
    gen_audio.gen(topic, CHARACTERS[character]["voiceid"], transcript)

    # generate images for the video
    print("generating images...")
    gen_images.gen(topic, image_prompts)

    # generate video by combining images, video, and audio
    # TODO

