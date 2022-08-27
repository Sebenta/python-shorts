#!/usr/bin/env python3
import moviepy.editor

video = moviepy.editor.VideoFileClip('./mp4/sample-mp4-file.mp4')
audio = video.audio
audio.write_audiofile('./mp3/sample-mp4-file.mp3')
