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
print("generate images...")
prompt_list = timestamps.split(']')

"""
prompt_list = [
    'A hand-drawn animated portrait of Grigori Rasputin with his iconic beard and intense eyes.',
    'A scene depicting Rasputin healing young Alexei while Tsar Nicholas II and Alexandra watch anxiously.',
    'A montage of Rasputins controversial behavior, including him flirting with women and drinking heavily in a dimly lit bar.',
    'A dramatic animation of the assassination attempt, showing Rasputin being offered poisoned wine and pastries, being shot multiple times, and being thrown into the icy Neva River.',
    'A somber image of the frozen Neva River with the text "The End of Rasputin" appearing on the screen.'
]
"""

gen_images.gen(prompt_list)

