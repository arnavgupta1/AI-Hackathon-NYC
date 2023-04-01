import gen_script
import gen_audio
import gen_images


# get user input for topic and character

# generate the transcript and timestamped image descriptions
print("generate script...")
[transcript, timestamps] = gen_script.gen()
print (transcript, timestamps)

# generate audio for the transcript
print("generate audio...")
gen_audio.gen(transcript, 'output.mp3')

# 
topic="rasputin"
print("generate images...")
timestamp_list = timestamps.split('\n')
prompt_list = []

for s in timestamp_list:
    for i, c in enumerate(s):
        if c.isalpha():
            new_s = s[i:]
            break
    prompt_list.append(new_s)

"""
prompt_list = [
    'A hand-drawn animated portrait of Grigori Rasputin with his iconic beard and intense eyes.',
    'A scene depicting Rasputin healing young Alexei while Tsar Nicholas II and Alexandra watch anxiously.',
    'A montage of Rasputins controversial behavior, including him flirting with women and drinking heavily in a dimly lit bar.',
    'A dramatic animation of the assassination attempt, showing Rasputin being offered poisoned wine and pastries, being shot multiple times, and being thrown into the icy Neva River.',
    'A somber image of the frozen Neva River with the text "The End of Rasputin" appearing on the screen.'
]
"""

gen_images.gen(topic, prompt_list)

