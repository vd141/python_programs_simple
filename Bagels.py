#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 23:19:33 2021

@author: victordinh
"""

# This is a program called bagels
# 
# Guess a 3 digit number based on clues
# Each guess gets one of 3 responses:
    # "Pico" when the guess has a correct digit in the wrong place
    # "Fermi" when the guess has a digit in the correct place
    # "Bagels" if your guess has no correct digits
   
import random    
   
input('Welcome to Bagels!\n')
input('You have 10 tries to guess a positive 3 digit integer with no leading zeroes or repeating digits.\n')
input('I\'ll give you feedback on each guess.\n')
input('"Pico" means you have a correct digit in the wrong place.\n')
input('"Fermi" means you have a correct digit in the right place.\n')
input('"Bagels" means your guess has no correct digits.\n')
input('Are you ready? I have thought of a 3 digit integer.\n')

random_int = random.randint(100,999)
random_int_str = str(random_int)
while len(set(random_int_str)) < len (random_int_str):
    random_int = random.randint(100,999)
    random_int_str = str(random_int)

print(random_int_str)

for x in range(10,0,-1):
    guess = input('What\'s your guess? You have {} guesses left.\n'.format(x))
    while not (guess.isnumeric() and (len(guess) == 3) and (float(guess) > 0) and (len(set(guess)) == len(guess))):
        guess = input('Your guess needs to be a 3 digit positive integer with no repeating digits. Try again.\n')
    if guess == random_int_str:
        print('You guessed the correct number. Congratulations!')
        break
    bagels_true = True
    for i in range(0,3):
        if guess[i] in random_int_str:
            bagels_true = False
            if guess[i] == random_int_str[i]:
                print('Fermi ')
            else:
                print('Pico ')
    if bagels_true:
        print('Bagels ')
    if x == 1:
        print('The number was {}. Try again next game!'.format(random_int_str))
        
    