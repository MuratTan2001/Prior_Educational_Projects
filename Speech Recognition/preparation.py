# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 23:36:27 2021S

@author: DELL
"""
import pydub
samplerate = 44100
####Appending audio files
sounds =          pydub.AudioSegment.from_file(file="Ses 001_sd.wav")
sounds = sounds + pydub.AudioSegment.from_file(file="Ses 002_sd.wav")
sounds = sounds + pydub.AudioSegment.from_file(file="Ses 003_sd.wav")
sounds = sounds + pydub.AudioSegment.from_file(file="Ses 004_sd.wav")
sounds = sounds + pydub.AudioSegment.from_file(file="Ses 005_sd.wav")
sounds = sounds + pydub.AudioSegment.from_file(file="Ses 006_sd.wav")
#  To find frame rate of song/file
print(sounds.frame_rate)   
# OUTPUT: 22050 
 
# To know about channels of file
print(sounds.channels) 
print(sounds.sample_width ) 
print(sounds.max)
print(len(sounds))
sounds.export(out_f="Recording.wav", format="wav")



####