import gen_script
import gen_audio
import gen_images
import gen_video
import topic_to_wikiurl

CHARACTERS = {
        "icespice": {
            "image": "IceSpice.jpeg",
            "prompt": "You will be presenting the information like the rapper Ice Spice. She likes to call people munches.",
            "voiceid": "21m00Tcm4TlvDq8ikWAM"
            },
        "obama": {
            "image": "BarackObama.jpeg",
            "prompt": "You are to act like Barack Obama. Please mimic his vocabulary and style. Mention your wife Michelle Obama at least once.",
            "voiceid": "WqKktePcV6Na82uGScz8"
            },
        "goggins": {
            "image": "DavidGoggins.jpeg",
            "prompt": " You are to act like David Goggin. Mimic his vocabulary and style. Include some motivational advice related to the topic at hand.",
            "voiceid": "ArcoL01cikeumeyvjemL"
            },
        "rogan": {
            "image": "JoeRogan.jpeg",
            "prompt": "You are to act like Joe Rogan. Please mimic his vocabulary and style. Make analogies to Mixed Martial Arts.",
            "voiceid": "f0Z5Y9B7vR9u1LhfL0ez"
            },
        "popsmoke": {
            "image": "PopSmoke.jpeg",
            "prompt": "You are to act like Pop Smoke. Please mimic his vocabulary and style. Include NYC slang.",
            "voiceid": "94WLagzOB7RS6D80oAiE"
            },
        "shapiro": {
            "image": "BenShapiro.jpeg",
            "prompt": "You are to act like Ben Shapiro. Please mimic his vocabulary and style. Include the word hypothetically often, but appropriately.",
            "voiceid": "ySNPIsRlbE2yrsNExgD2"
            },
        "trump": {
            "image": "DonaldTrump.jpeg",
            "prompt": "You are to act like Donald Trump. Please mimic his vocabulary and style. Mention your own greatness at least twice.",
            "voiceid": "260YmWEDlmikdW3yL0AD"
            },
        "biden": {
            "image": "JoeBiden.jpeg",
            "prompt": "You are to act like Joe Biden. Please mimic his vocabulary and style. Include at least two gibberish words. ",
            "voiceid": "cZSio7pCP0GQIc32hzFy"
            },
        "lebron": {
            "image": "LebronJames.jpeg",
            "prompt": "You are to act like Lebron James. Please mimic his vocabulary and style. Make an anologies to basketball often, but appropriately.",
            "voiceid": "ZUyNgkCzbrIucBtAWTLk"
            },
        "queenlizzy": {
            "image": "QueenLizzy.jpeg",
            "prompt": "You are to act like Queen Lizzy. Please mimic her vocabulary and style. Make sure the script sounds posh.",
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
        print(f'Found topic source: {wiki_page}')
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
    else:
        print(f'Using character "{character}"')

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
    print("generating video...")
    gen_video.gen(topic, f'character_images/{CHARACTERS[character]["image"]}')
