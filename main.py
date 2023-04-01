import gen_script
import gen_audio
import gen_images

prompt_list = [
    'A hand-drawn animated portrait of Grigori Rasputin with his iconic beard and intense eyes.',
    'A scene depicting Rasputin healing young Alexei while Tsar Nicholas II and Alexandra watch anxiously.',
    'A montage of Rasputins controversial behavior, including him flirting with women and drinking heavily in a dimly lit bar.',
    'A dramatic animation of the assassination attempt, showing Rasputin being offered poisoned wine and pastries, being shot multiple times, and being thrown into the icy Neva River.',
    'A somber image of the frozen Neva River with the text "The End of Rasputin" appearing on the screen.'
]


# [transcript, timestamps] = gen_script.gen()
# print ("noice", transcript, timestamps)

# gen_audio.gen('output.mp3')

gen_images.gen(topic, prompt_list)

