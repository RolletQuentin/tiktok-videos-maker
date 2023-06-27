import random
from moviepy.editor import *


def crop_bg_video(bg_video):
    # Charger la vidéo de fond
    background_video = bg_video

    # Déterminer les dimensions du recadrage
    target_width = 1080
    target_height = 1920

    # Resize la video
    background_video = background_video.resize(height=1920)

    # Calculer les coordonnées du recadrage
    x_center = background_video.size[0] / 2
    y_center = background_video.size[1] / 2
    x_start = x_center - target_width / 2
    y_start = y_center - target_height / 2
    x_end = x_center + target_width / 2
    y_end = y_center + target_height / 2

    # Recadrer la vidéo de fond
    cropped_video = background_video.crop(
        x1=x_start, y1=y_start, x2=x_end, y2=y_end)

    # Redimensionner la vidéo recadrée au format cible
    final_video = cropped_video.resize((target_width, target_height))

    return final_video


def create_synced_videos(story_folder, supported_languages, title):

    for language in supported_languages:
        # load audio files
        audio_title = AudioFileClip(
            f"{story_folder}/{language}_title.wav").set_start(0.5)

        audio = AudioFileClip(
            f"{story_folder}/{language}_text.wav").set_start(1 + audio_title.duration)
        video_duration = audio_title.duration + audio.duration + 1.5

        # load background video
        random_start = random.randint(0, int(4810 - video_duration))
        background_video = VideoFileClip("minecraft_video.mp4").subclip(
            random_start, random_start + video_duration).set_audio(0)

        # resize the background video
        final_video = crop_bg_video(background_video)

        # combine background_video and subtitles and audio
        final_video = final_video.set_audio(CompositeAudioClip(
            [audio_title, audio]))

        # save the video
        final_video.write_videofile(
            f"{story_folder}/{language}_{title.replace(' ', '-')}.mp4", fps=24)


if __name__ == "__main__":

    create_synced_videos("story_01")
