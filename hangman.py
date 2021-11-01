#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 12:59:09 2021

@author: ciaranmcdonnell
"""

"""
Basic game of hangman that I can play.
"""   
import numpy as np
from english_words import english_words_lower_set as words
import random as rand



words_array = list(words)

guess_word = rand.choice(words_array)
g_word_list = list(guess_word)

blanks =''
for i in range(len(guess_word)):
    blanks += '_ '
    
blanks_list = list(blanks)    

lives = 6
win = False

play = input('========== Welcome to Hangman! ========== \n\n     Are you ready to play? y/n:  ')

if play == 'y':
    
    print('\nThe computer has chosen a word:  ' + ''.join(blanks_list))
    while win == False: 
        
        guess_letter = input('Please pick a letter: ').lower()
        
        if len(guess_letter)!=1:
            print('\n Oops! Only one letter at a time!')
        else:
            if guess_letter in guess_word:
                print('\nWell done! You got one!')
                ii = np.where(np.array(g_word_list) == guess_letter)[0]
                for j in ii:
                    blanks_list[2*j] = guess_letter
                print('\n' + ''.join(blanks_list) + '\n\nGo again!\n=======================') 
            else:
                lives -= 1
                if lives ==0:
                    print('\nYou are out of lives! Better luck next time! \nThe word was ' + guess_word)
                    break
                print('\n' + guess_letter + ' is not in the word! You have ' + str(lives) + ' lives left.')
                print('\n' + ''.join(blanks_list) + '\n\nGo again!\n=======================')
        if blanks_list.count('_') == 0:
            print("\nCongratulations you won!")
            break
print('\nHave a wonderful day!')    