# -*- coding: utf-8 -*-
"""Abhinav Conversion Systems.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1M1PfetgB16Z2pX_diLB0s1Ab3e1WRttC

### Install the SpeechRecognition package

# Audio To Text Conversion
"""

!pip install SpeechRecognition

"""**Function for SpeechToTextConverter**"""

import speech_recognition as sr
#Initiаlize  reсоgnizer  сlаss  (fоr  reсоgnizing  the  sрeeсh)
r = sr.Recognizer()
# Reading Audio file as source
#  listening  the  аudiо  file  аnd  stоre  in  аudiо_text  vаriаble
with sr.AudioFile('/content/Sample.wav') as source:
    audio_text = r.listen(source,phrase_time_limit=100)
# recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
    try:
        # using google speech recognition
        text = r.recognize_google(audio_text)
        print('Converting audio transcripts into text ...')
        print(text)
    except:
         print('Sorry.. run again...')

from google.colab import drive
drive.mount('/content/drive')

"""***For larger audio conversions refer to the article*** [Speech2Text](https://www.thepythoncode.com/article/using-speech-recognition-to-convert-speech-to-text-python)

# Image To Text

**Install Package**
"""

!sudo apt install tesseract-ocr
!pip install pytesseract
!pip install Pillow==9.0.0

"""### **Function for Image to text**"""

from google.colab import files

uploaded = files.upload()

import pytesseract
from PIL import Image

extractedInformation = pytesseract.image_to_string(Image.open('/content/logo.png'))

print(extractedInformation)

"""# Video To Audio

### **Install necessary packages**
"""

!pip install moviepy

"""**Program for converting video to audio**"""

from moviepy.editor import VideoFileClip
import os
uploaded = files.upload()
def convert_video_to_audio_moviepy(video_file, output_ext="mp3"):
    """Converts video to audio using MoviePy library
    that uses `ffmpeg` under the hood"""
    filename, ext = os.path.splitext(video_file)
    clip = VideoFileClip(video_file)
    clip.audio.write_audiofile(f"{filename}.{output_ext}")

convert_video_to_audio_moviepy('/content/videoplayback.mp4')

