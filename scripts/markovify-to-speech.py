#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 19:05:36 2018

@author: Phil
"""
# import libraries
import markovify as m
from playsound import playsound
from gtts import gTTS

# get raw text as string
with open("../poems/TheWasteland_TSEliot.txt") as wasteland:
    wasteland = wasteland.read()

with open("../poems/Poems1918-21_EzraPound.txt") as pound:
    pound = pound.read()

with open("../poems/williams_improvisations.txt") as improv:
    improv = improv.read()
    
# build the model
wasteland_model = m.Text(wasteland) #text_model = markovify.Text(text)
pound_model = m.Text(pound)
improv_model = m.Text(improv)

# synthesize the model
synthesized_model = m.combine([wasteland_model, pound_model, improv_model], [1,1,1.5])

## print randomly-generated sentences 
#for i in range(0,11):
#    print synthesized_model.make_sentence()
    
# print randomly-generated sentences using lists
my_list = []
for i in range(1,11):
    my_list.append(synthesized_model.make_short_sentence(140) + \
                   synthesized_model.make_short_sentence(140))

 # get raw text as string with (w) write or (a) append option
with open("../poems/markov-generated-poem-iterations.md", "a") as f:
    
# write the text generated from the markov model
    for item in my_list:
        f.write(item)

    
#print to variable 
#with open("generated-poem.md", "w") as f:
#    f.write("## Retrospective Collaboration")
#    f.write("\n")
#    f.write("\n")
#    for i in range(3):
#        poem = synthesized_model.make_sentence() 
#        print synthesized_model.make_sentence()
#        f.write(poem)
#        f.write("\n")
    
    
#with open("generated-poem.md", "w") as f:
#    f.write("## Title")
#    f.write("\n")
#    f.write("\n")
#    f.write("```")
#    f.write(poem)
#    f.write("```")


#with open("generated-poem.md", "w") as f:
#    f.write("""
## Title
#```
#{poem}
#```
#""".format(poem=poem))

# text to speech
tts = gTTS(text=markov_poem, lang='en')

# write audio file
tts.save("../poems/markovified-poem.mp3")

# play audio file
playsound("../poems/markovified-poem.mp3")
