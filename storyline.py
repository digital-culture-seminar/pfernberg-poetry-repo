#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 19:16:46 2018

@author: Phil
"""

import random

# set the random seed
random.seed()

# lists of words
nouns1 = ["garbage man", "darling", "breath", "words", "something", "script", "marmot", "sloth", "avatar", \
         "jabberwocky", "person", "lines", "mile mark", \
         "nurse"]
nouns2 = ["garbage man", "darling", "breath", "words", "something", "script", "marmot", "sloth", "avatar", \
         "jabberwocky", "person", "lines", "mile mark", \
         "nurse"]
verbs = ["laugh", "speak", "recite", "hush", "break", "save", "waste", "take", "make", "mold", \
         "sleep", "read", "cross"]
verbs2 = ["refine", "rake", "hold", "berate", "waste", "carry", "knead", "make", "fabricate", "scuplt", \
          "smooth", "corrugate"]
verbs3 = ["laugh", "speak", "recite", "hush", "break", "save", "waste", "take", "make", "mold", \
         "sleep", "read", "cross"]
verbs4 = ["refine", "rake", "hold", "berate", "waste", "carry", "knead", "make", "fabricate", "scuplt", \
          "smooth", "corrugate"]
adjectives = ["saucy", "intangible", "impossible", "ineffable", "playful", "stupefied", "lobotomized", \
              "sleepy", "buxom", "arrogant","stealthy", "mechanical", "dapper", "erudite", "insatiable",\
              "breached", "ancient"]
adverbs = ["loudly", "soundly", "tersely", "playfully", "proudly", "tearfully", "mindfully", \
           "inexplicably", "boldly", "gently", "condescendingly", "disdainfully", "perfectly", "patiently"]



def random_word_choice():
    # select random words from lists
    noun = random.choice(nouns1)
    noun2 = random.choice(nouns2)
    verb = random.choice(verbs)
    verb2 = random.choice(verbs2)
    verb3 = random.choice(verbs3)
    verb4 = random.choice(verbs4)
    adjective = random.choice(adjectives)
    adverb = random.choice(adverbs)
    return noun, verb, adjective, adverb

whitespace = " "


story = ["We speak the {noun} that we've never said.",
         "You {verb} from a {noun} that you've never read.",
         "Hush now, my {noun}, there is no need to {verb} your {noun2}.",
         "I will {verb} you and {verb2} you and {verb3} you and {verb4} you and save you from what you've become."]



#def meta_story():
#    for i in xrange(0,6):
#        tell_story()

def tell_story(noun):
    for line in story:
#        noun, verb, adjective, adverb = random_word_choice()
#        print line.format(adjective=adjective, noun=noun, adverb=adverb, verb=verb)
        print line.format(
                adjective=random.choice(adjectives), 
                noun=random.choice(nouns1),
                noun2=random.choice(nouns2)
                adverb=random.choice(adverbs), 
                verb=random.choice(verbs))
        
def meta_story():
    for noun in nouns1:
        tell_story(noun)
        if nouns1 == nouns1[2]: break
        print ("")
        
meta_story()

# print the shuffled list of adjectives with increasing whitespace
i = 0
print "You are: "
print whitespace 
for adjective in adjectives:
    i = i + 1
    whitespace = " " * i
    print whitespace + adjective
    print whitespace
            
print "but it's okay, we can work this out."
print "Forgiveness is my middle name."






