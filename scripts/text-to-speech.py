#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 18:28:15 2018

@author: Phil
"""

# import libraries
from playsound import playsound
from gtts import gTTS

# text to speech
tts = gTTS(text="Helloooo", lang="en")

# write audio file
tts.save("../poems/helloooo.mp3")

# play audio file
playsound("helloooo.mp3")