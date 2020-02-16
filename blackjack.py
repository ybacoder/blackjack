"""
Yacub Bholat
Data Analysis and Visualization Boot Camp
Blackjack Homework (Optional)
Due: 23 February 2020
"""

import random as r


class Card():
    # add init
    # give card attributes: value, suit, and score
    # maybe initialize ace as 11 and flip it to a 1 if the score is > 21


class Deck():
    # pass number of decks as an argument and create the overall Deck object
    # one loop for number of decks, one loop for 
    # create a deck using a double for loop either in init or passed as argument
    def shuffle():
        # call this function in the init() method
        return "shuffle"

    def draw():
        # use a pop method to remove card and return it
        return "draw"


class Player():
    # player should get some cards on init() accessing deck object
    
    def hit():
        # use pop method to remove card from deck and add to player hand attribute
        return "add_card"

    def score():
        # score the hand
        # need to keep track of aces to pick the best hand
        return "score"

    def play():
        # show you your hand
        # ask if you want to hit
        # then score your hand
        # if hand score > 21 you lose
        # if no hit, player turn ends
        return "player play"


class Dealer(Player):
    # dealer should get some cards on init() accessing deck object
    def initial_hand():
        # show dealer's card with one card hidden
        return "show dealer hand"
    
    def play():
        # flip over hidden card
        # play while hand is less than or equal to 16
        # if > 21, bust
        # if > 16 but less than player, player wins
        # else dealer wins
        return "dealer play"


def setup_game():
    return "setup"

def play_game():
    return "play game"