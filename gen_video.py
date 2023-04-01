import os
from moviepy.editor import ImageClip, AudioFileClip, concatenate_videoclips, concatenate_audioclips


def gen(source_folder):
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

    image_clips = [ImageClip(img) for img in image_files]
    audio_clips = [AudioFileClip(audio) for audio in audio_files]

    for i in range(len(image_clips)):
        image_clips[i] = image_clips[i].set_duration(audio_clips[i].duration)
        image_clips[i].fps = 24  # Set the fps for each ImageClip

    video = concatenate_videoclips(image_clips)
    audio = concatenate_audioclips(audio_clips)

    video = video.set_audio(audio)
    video.write_videofile(f"{source_folder}/video.mp4")


# for quick testing out of pipeline
if __name__ == "__main__":
    print("testing video generation")
    gen("Rasputin")
