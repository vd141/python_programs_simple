# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 23:26:33 2021

@author: victo
"""
# 12/20/2021: putting this back on the shelf for now. Exploring generative art


# Blackjack
# 52 cards in a deck, 4 suites, 13 cards each
# get as close to 21 as you can without going over
# Kings, Queens, and Jacks are worth 10 points
# Aces are worth 1 or 11 points
# Cards 2 through 10 are worth their face value
# (H)it to take another card
# (S)tand to stop taking cards
# On your first play, you can double down to double your bet, but you must hit once before standing
# In the case of a tie, the bet is returned to the player
# The dealer stops hitting at 17
# Money: 5000 to start with
# First option is to decide how much money to bet. Or QUIT
# Dealer has 2 cards, 1 face up and one face down
# Player has two cards that can be seen. Player can choose to hit, stay, or double down

# Create card deck module 
    # card deck class
    # Each card has a status: either played or still in the deck
    # method to draw random card
    
    # card deck rendering function
    # take in card values
    # can render cards in a 1x1 or 2x1 space
    
    # UPDATE: card deck modules exist. Encountering difficulty using in standalone Spyder as it is not recognizing these newly installed packages
    # May revert back to creating my own module

# player class
# Properties:
    # Unbet money
    # bet money
    # cards held
# Methods
    # Ask how much to bet
    # Ask what action to take (Hit, stay, or duoble down - only on first round)
    
# dealer class
# Properties:
    # Cards held
    # knows which round of game it is
    # A sum of money much greater than the player's sum
# Methods:
    # Draw cards from card deck until limit is reached (17)
    
    
# Control game flow
# decides what actions are taken and when