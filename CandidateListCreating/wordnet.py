#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 14:35:41 2020

@author: muhammedburakgormus
"""
from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize

def get_hyper_set(syn_set):
    hyper_set = set()
    for i in syn_set:
        listt = i.hypernyms()
        for y in listt:
            for t in y.lemmas():
                hyper_set.add(t.name())
    return hyper_set

def get_hypo_set(syn_set):
    hypo_set = set()
    for i in syn_set:
        listt = i.hyponyms()
        for y in listt:
            for t in y.lemmas():
                hypo_set.add(t.name())
    return hypo_set

def get_wordnet_each_word(word,length):
    #hyponyms/hypernyms/synonyms
    #iki kelimeliler asad_aslkma şeklinde
    #understood !!!
    syn_set = wordnet.synsets(word)
    name_set = set()
    for i in syn_set:
        for j in i.lemmas():
            name_set.add(j.name())
    hyper_set1 = get_hyper_set(syn_set)
    hypo_set1 = get_hypo_set(syn_set)

    hyper_set2 = set()
    for i in hyper_set1:
        syn_set_for_i = wordnet.synsets(i)   
        for k in get_hyper_set(syn_set_for_i):
            hyper_set2.add(k)

    hypo_set2 = set()     
    for i in hypo_set1:
        syn_set_for_i = wordnet.synsets(i)   
        for k in get_hypo_set(syn_set_for_i):
            hypo_set2.add(k)
    
    complete_words = set()
    [complete_words.add(i) for i in name_set if len(i)==length]
    [complete_words.add(i) for i in hyper_set1 if len(i)==length]
    #[complete_words.add(i) for i in hyper_set2 if len(i)==length]
    [complete_words.add(i) for i in hypo_set1 if len(i)==length]
    #[complete_words.add(i) for i in hypo_set2 if len(i)==length]

    return complete_words

def get_wordnet(clue,length):
    name_set = set()
    words_list = word_tokenize(clue)
    for i in words_list:
        for j in get_wordnet_each_word(i,length):
            name_set.add(j)
    return list(name_set)
    
#print(get_wordnet("Salad green with a peppery taste",5))
#print(get_wordnet("Less restricted",5))



