#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 19:00:14 2018

@author: Phil
"""

install markovify

# import libraries
import markovify

# get raw text as string
with open("../readings/mallarme-a-roll-of-the-dice.txt") as f:
    text = f.read()
    
    # build the model
text_model = markovify.NewlineText(text) #text_model = markovify.Text(text)

# print three randomly-generated sentences of no more than 140 characters
for i in range(3):
    print text_model.make_short_sentence(140)
    