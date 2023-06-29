# TikTok Videos Maker

With this project, you can create videos for TikTok. For now, it's just an experimental version, many changes would be come.

## Installation

To install this project, you can clone the project and run `pip` command :
```
git clone https://github.com/RolletQuentin/tiktok-videos-maker
cd tiktok-videos-maker
pip install -r requirements.txt
```

## Prerequisites
You must have a video called `minecraft_video.mp4` at the root of the project. It is the background use for the videos. Here is the link of the video I use : https://www.youtube.com/watch?v=n_Dv4JMiwK8

## Run

To launch the API :
```
python3 main.py --api --port 8000
```

To create a video with command line :
```
python3 main.py --title "Title example" --description "The content of the video"
```

This command will create a new directory, called `stories`, where all the videos will be saved. In this directory, you can find folders `story_XX`. In these folders, you can find the auto-generated videos in three languages (english, french and spannish).

## Features
- [x] Create videos for TikTok
- [x] Make an API
- [ ] You can choose the languages
- [ ] Web User Interface
- [ ] Generate images with Stable Diffusion to make beautiful videos

