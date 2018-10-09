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

# print three randomly-generated sentences of no more than 140 characters
for i in range(6):
    print synthesized_model.make_sentence()
   
    
