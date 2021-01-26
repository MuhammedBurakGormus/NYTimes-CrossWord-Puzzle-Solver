#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 22:57:14 2020

@author: muhammedburakgormus
"""

from gensim.models import Word2Vec, KeyedVectors
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import nltk

model = KeyedVectors.load_word2vec_format("GoogleNews-vectors-negative300.bin",binary=True,limit=100000,unicode_errors='ignore')

def get_word2vector(clue,length):
    #taking the clue string and length of the answer
    clue = clue.lower()
    words = word_tokenize(clue)
    filtered_words = []
    stop_words = stopwords.words("english")
    stop_words.append('the')
    for i in words: 
        if i not in stop_words:
            filtered_words.append(i)
    #print(filtered_words)
    vector_sum = 0
    for word in filtered_words:
        if word in model:
            vector_sum = vector_sum + model[word]
    top20models = model.most_similar([vector_sum],topn=20)
    word_set = set()
    for candidates in top20models: 
        if len(candidates[0]) == length:
            word_set.add(candidates[0])
    return list(word_set)

#print(get_word2vector("Harbor cities",5))
#print(word_2_vector("Historical artifact",5))
#print(get_word2vector("___ Hotel, iconic building overlooking Central Park",5))
#print(get_word2vector('"The Communist Manifesto" co-author',4))
