#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 19:46:13 2020

@author: muhammedburakgormus
"""

from wordnet import get_wordnet
from wikisearch import get_wikipedia
from word2vec import get_word2vector
from PytonDictionary import dictionary
import puzzle_demo2   
       
loaded_puzzle = puzzle_demo2.puzzle("23-12-2020.save")
intersection_boxes = loaded_puzzle.intersections
across_len = loaded_puzzle.across_answer_lengths
down_len = loaded_puzzle.down_answer_lengths
across_clues = loaded_puzzle.clues_across
down_clues = loaded_puzzle.clues_down

#######################################################################################################
#######################################################################################################
def get_candidates(across_clues,across_len,down_clues,down_len):
    cand_dict = {}
    for i in down_clues:
        number = i[0]
        clue = i[1]
        for j in down_len:
            if number == j[0]:
                candidate_list = []
                clue_len = j[1]
                try:
                    wiki_list = get_wikipedia(clue,clue_len)
                    wordnet_list = get_wordnet(clue,clue_len)
                    vec_list = get_word2vector(clue,clue_len)
                    py_list = dictionary(clue,clue_len)
                    [candidate_list.append(i) for i in wiki_list]
                    [candidate_list.append(i) for i in wordnet_list]
                    [candidate_list.append(i) for i in vec_list]
                    [candidate_list.append(i) for i in py_list]
                    cand_dict[clue] = candidate_list
                except:
                    cand_dict[clue] = []
    for i in across_clues:
        number = i[0]
        clue = i[1]
        for j in across_len:
            if number == j[0]:
                candidate_list = []
                clue_len = j[1]
                try:
                    wiki_list = get_wikipedia(clue,clue_len)
                    wordnet_list = get_wordnet(clue,clue_len)
                    vec_list = get_word2vector(clue,clue_len)
                    py_list = dictionary(clue,clue_len)
                    [candidate_list.append(i) for i in wiki_list]
                    [candidate_list.append(i) for i in wordnet_list]
                    [candidate_list.append(i) for i in vec_list]
                    [candidate_list.append(i) for i in py_list]
                    cand_dict[clue] = candidate_list
                except:
                    cand_dict[clue] = []
    return cand_dict
#######################################################################################################
#######################################################################################################
def ranking_candidates(intersection_boxes,across_clues,across_len,down_clues,down_len,dict_puzzle):
    for i in intersection_boxes:
        for j in i:
            if len(j) != 0:
                first_el = j[0]
                second_el = j[1]
                type_first = first_el[0]
                type_second = second_el[0]
                number_first = first_el[1]
                number_second = second_el[1]
                letter_first_index = first_el[2]
                letter_second_index = second_el[2]
                if type_first == "Across":
                    for k in across_clues:
                        if k[0] == number_first:
                            clue_across = [k][0][1]
                            clue_across_answers = dict_puzzle[clue_across]
                if type_second == "Down":
                    for u in down_clues:
                        if u[0] == number_second:
                            clue_down = [u][0][1]
                            clue_down_answers = dict_puzzle[clue_down]
                for across_answers in clue_across_answers:                    
                    for down_answers in clue_down_answers:
                        if across_answers[0][letter_first_index] == down_answers[0][letter_second_index]:
                            new_across_val = across_answers[2] + 1
                            across_answers[2] = new_across_val
                            down_answers[2] = down_answers[2] + 1
    return dict_puzzle        
#######################################################################################################
#######################################################################################################
def checking_occurences(puzzle_dict):
    #checking whether the same word appears from different sources;
    #if it is the case, summing the ranks up and making it one element     
    for i in puzzle_dict:
        words = []
        for j in puzzle_dict[i]:
            if j[0] not in words:
                words.append(j[0])
            else:
                puzzle_dict[i].remove(j)
                for k in puzzle_dict:
                    for m in puzzle_dict[k]:
                        if m[0] == j[0]:
                            puzzle_dict[k].append([j[0],"intersected",j[2] * 2])
                            puzzle_dict[k].remove(m)
    return puzzle_dict
#######################################################################################################
#######################################################################################################
def select_best_candidates(candidate_list):
    ranking_list = []
    best_candidates = []
    for clues in candidate_list:
        ranking_list.append(clues[2])
    ranking_list.sort(reverse=True)
    
    best_3_scores = ranking_list[0:3]
    for clues in candidate_list:
        if clues[2] in best_3_scores:
            best_candidates.append(clues)
    return best_candidates

def select__best_candidates_for_puzzle(dict_puzzle):
    for clues in dict_puzzle:
        best_clues = select_best_candidates(dict_puzzle[clues])
        dict_puzzle.update({clues:best_clues})
    return dict_puzzle
#######################################################################################################
#######################################################################################################
def get_grid_letters(intersection_boxes,across_clues,across_len,down_clues,down_len,dict_puzzle):
    grid_letters_dict = {}
    counter = 0
    for i in intersection_boxes:
        letters = {}
        for j in i:
            counter = counter + 1
            if j:
                first_el = j[0]
                second_el = j[1]
                type_first = first_el[0]
                type_second = second_el[0]
                number_first = first_el[1]
                number_second = second_el[1]
                letter_first_index = first_el[2]
                letter_second_index = second_el[2]
                if type_first == "Across":
                    for k in across_clues:
                        if k[0] == number_first:
                            clue_across = [k][0][1]
                            clue_across_answers = dict_puzzle[clue_across]
                if type_second == "Down":
                    for u in down_clues:
                        if u[0] == number_second:
                            clue_down = [u][0][1]
                            clue_down_answers = dict_puzzle[clue_down]   
                for across_answers in clue_across_answers:   
                    if across_answers[0][letter_first_index] not in letters:
                        letters.update({ across_answers[0][letter_first_index]:1})
                    else:
                        new_val = letters[across_answers[0][letter_first_index]] + 1
                        letters.update({ across_answers[0][letter_first_index]:new_val})
                for down_answers in clue_down_answers:   
                    if down_answers[0][letter_second_index] not in letters:
                        letters.update({ down_answers[0][letter_second_index]:1})
                    else:
                        new_val = letters[down_answers[0][letter_second_index]] + 1
                        letters.update({ down_answers[0][letter_second_index]:new_val})
                grid_letters_dict.update({counter:letters})
            else:
                grid_letters_dict.update({counter:[]})
    return grid_letters_dict
#######################################################################################################               
#######################################################################################################               
def point_rank(dict_puzzle,grid_letters,intersection_boxes):
    last_point_dict ={}
    counter= 0
    for i in intersection_boxes:
        for j in i:
            counter = counter + 1
            if j:
                first_el = j[0]
                second_el = j[1]
                type_first = first_el[0]
                type_second = second_el[0]
                number_first = first_el[1]
                number_second = second_el[1]
                letter_first_index = first_el[2]
                letter_second_index = second_el[2]
                if type_first == "Across":
                    for k in across_clues:
                        if k[0] == number_first:
                            clue_across = [k][0][1]
                            clue_across_answers = dict_puzzle[clue_across]
                if type_second == "Down":
                    for u in down_clues:
                        if u[0] == number_second:
                            clue_down = [u][0][1]
                            clue_down_answers = dict_puzzle[clue_down]
                for across_answers in clue_across_answers:
                    point = grid_letters[counter][across_answers[0][letter_first_index]]
                    if across_answers[0] not in last_point_dict:
                        last_point_dict.update({across_answers[0]:point})
                    else:
                        x = last_point_dict[across_answers[0]] + point
                        last_point_dict.update({across_answers[0]:x})
                    
                for down_answers in clue_down_answers:
                    point = grid_letters[counter][down_answers[0][letter_second_index]]
                    if down_answers[0] not in last_point_dict:
                        last_point_dict.update({down_answers[0]:point})
                    else:
                        x = last_point_dict[down_answers[0]] + point
                        last_point_dict.update({down_answers[0]:x})
    
    for i in dict_puzzle:
        for j in dict_puzzle[i]:
            for k in last_point_dict:
                if k == j[0]:
                    j[2] = last_point_dict[k]
                        
    return dict_puzzle
#######################################################################################################               
#######################################################################################################                                   
def one_candidate(puzzle_dict,grid_letters,intersection_boxes):
    counter_list = []
    for i in puzzle_dict:
        counter_list.append(len(puzzle_dict[i])) 
    for i in puzzle_dict:
        rank_val = []
        if len(puzzle_dict[i])>1:
            for j in puzzle_dict[i]:
                rank_val.append(j[2])
            min_val = min(rank_val)
            for k in puzzle_dict[i]:   
                if k[2] == min_val:
                    puzzle_dict[i].remove(k)
            new_dict= puzzle_dict
            grid_letters = get_grid_letters(intersection_boxes,across_clues,across_len,down_clues,down_len,new_dict)
            ranked_new_dict = point_rank(new_dict,grid_letters,intersection_boxes)
            one_candidate(ranked_new_dict,grid_letters,intersection_boxes)
    return puzzle_dict

def main():
    dict_puzzle = get_candidates(across_clues,across_len,down_clues,down_len)
    ranked_puzzle_dict = ranking_candidates(intersection_boxes,across_clues,across_len,down_clues,down_len,dict_puzzle)
    removed_dict = checking_occurences(ranked_puzzle_dict)    
    filtered_puzzle_dict = select__best_candidates_for_puzzle(removed_dict)
    grid_letters = get_grid_letters(intersection_boxes,across_clues,across_len,down_clues,down_len,filtered_puzzle_dict)
    ranked_sol = point_rank(filtered_puzzle_dict,grid_letters,intersection_boxes)
    final = one_candidate(ranked_sol,grid_letters,intersection_boxes)
    return final

print(main())


    






