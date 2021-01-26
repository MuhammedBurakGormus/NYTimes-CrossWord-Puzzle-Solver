#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 00:08:22 2020

@author: muhammedburakgormus
"""
import re
import wikipedia
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk.corpus import stopwords

def get_wikipedia(clue,length):
    stop_words = stopwords.words("english")
    word_set = set()
    try: 
        search = wikipedia.search(clue)
        for elements in search:
            words_list = word_tokenize(elements)
            for i in words_list:
                if len(i) == length:
                    if i.isalpha():
                        if i not in stop_words:
                            word_set.add(i)
    except wikipedia.exceptions.DisambiguationError as e:
        pass
    try:
        if re.findall(r'"([^"]*)"', clue):
            special_str = re.findall(r'"([^"]*)"', clue)
            summary = wikipedia.summary(special_str,sentences = 1)
            word_list_2 = word_tokenize(summary)
            for s in word_list_2:
                if len(s) == length:
                    if s.isalpha():
                        if s not in stop_words:
                            word_set.add(s)
    except wikipedia.exceptions.DisambiguationError as e:
        pass
    return list(word_set)
    

#print(get_wikipedia("Sammy with 609 career home runs",4))
#print(get_wikipedia("___ Tanden, Biden's pick to lead the O.M.B.",5))
#print(get_wikipedia("Lincoln Center performance",5))
#print(get_wikipedia('"The Communist Manifesto" co-author',4))

    

        






