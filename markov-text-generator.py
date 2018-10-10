#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 19:00:14 2018

@author: Phil
"""


# import libraries
import markovify as m

# get raw text as string
with open("TheWasteland_TSEliot.txt") as wasteland:
    wasteland = wasteland.read()

with open("Poems1918-21_EzraPound.txt") as pound:
    pound = pound.read()

with open("williams_improvisations.txt") as improv:
    improv = improv.read()
    
# build the model
wasteland_model = m.NewlineText(wasteland) #text_model = markovify.Text(text)
pound_model = m.NewlineText(pound)
improv_model = m.NewlineText(improv)

# synthesize the model
synthesized_model = m.combine([wasteland_model, pound_model, improv_model], [1,1,1.5])

## print randomly-generated sentences 
#for i in range(0,11):
#    print synthesized_model.make_sentence()
    
# print randomly-generated sentences using lists
my_list = []
for i in range(0,11):
    my_list.append(synthesized_model.make_sentence(140))

# get raw text as string with (w) write or (a) append option
with open("generated-poem.md", "w") as f:
    
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