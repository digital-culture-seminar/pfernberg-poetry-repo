i#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 20:10:04 2018

@author: Phil
"""

import random

random.seed()

names = ("Johnny", "Saoirse", "Liv")
name = random.choice(names)
pronouns = ("he", "she")
pronoun = random.choice(pronouns)

# print the opening lines of the story
print "The night of the hurricane, 11:24 pm, \
my young friend {name} told me a story. \
{pronoun} had some old bones in the closet; \
a colored history paid for with a fistful of spilt blood, \
determined by the fate of a single die.".format(name=name, pronoun=pronoun.capitalize())

roll = random.randint(1,6)
print "{name} rolled a {roll}".format(name=name, roll=roll)

if roll == 1:
    print "Bad luck!"
    
elif roll == 6:
    print "YES!"
    
else:
    print "Not so bad luck..."
    
    
