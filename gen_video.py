import os
import numpy as np
from moviepy.editor import ImageClip, AudioFileClip, concatenate_videoclips, concatenate_audioclips
from PIL import Image

def gen(source_folder, profile_image):
    print(f'using source ./{source_folder}')
    audio_files = []
    image_files = []

    for file in os.listdir(source_folder):
        if file.startswith("audio") and file.endswith(".mp3"):
            audio_files.append(os.path.join(source_folder, file))
        elif file.startswith("image") and file.endswith(".jpg"):
            image_files.append(os.path.join(source_folder, file))

    audio_files.sort(key=lambda x: int(x.split("audio")[-1].split(".mp3")[0]))
    image_files.sort(key=lambda x: int(x.split("image")[-1].split(".jpg")[0]))

    # make profile image the first image in the slideshow
    image_files[:0] = [profile_image]

    video_clips = []
    for img, audio in zip(image_files, audio_files):
        audio_clip = AudioFileClip(audio)
        duration = audio_clip.duration
        im = Image.open(img)
        im_resized = im.resize((im.width, 1024), Image.ANTIALIAS)
        np_im_resized = np.array(im_resized)
        video_clip = ImageClip(np_im_resized).set_duration(duration)
        video_clips.append(video_clip)

    video = concatenate_videoclips(video_clips, method="compose")
    audio = concatenate_audioclips([AudioFileClip(audio) for audio in audio_files])

    video = video.set_audio(audio)
    video.write_videofile(f"{source_folder}/video.mov", fps=24, codec="libx264", audio_codec="aac")

if __name__ == "__main__":
    print("testing video generation")
    gen("Emu War", "character_images/BenShapiro.jpeg")
