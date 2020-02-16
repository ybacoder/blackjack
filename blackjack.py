"""
Yacub Bholat
Data Analysis and Visualization Boot Camp
Blackjack Homework (Optional)
Due: 23 February 2020
"""

import random as r


class Card():
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        
        if self.value in [2, 3, 4, 5, 6, 7, 8, 9, 10]:
            score = self.value
        elif self.value in ["J", "Q", "K"]:
            score = 10
        elif self.value == "A":
            # initialize A as 11 - flip it to a 1 later if the hand score is > 21
            score = 11

        self.score = score
    
    def __repr__(self):
        return f"{self.value}{self.suit} with score {self.score}"


class Deck():
    def __init__(self, num_decks):
        self.num_decks = num_decks
        self.deck = []

        for n in range(self.num_decks):
            for value in [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]:
                for suit in ["D", "C", "H", "S"]:
                    self.deck.append(Card(value, suit))
        
        self.shuffle()
    
    def __repr__(self):
        for card in self.deck:
            print(card)
        return ""

    def __len__(self):
        return len(self.deck)

    def shuffle(self):
        # call this function in the init() method
        return r.shuffle(self.deck)

    def draw(self):
        # use a pop method to remove card and return it
        return self.deck.pop()



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


if __name__ == "__main__":
    # code to test that specifying number of decks works correctly
    deck = Deck(1)
    print(f"Cards in one deck: {len(deck)}")
    deck = Deck(2)
    print(f"Cards in two decks: {len(deck)}")
    print("\n")

    # code to test that deck.draw() method works correctly
    deck = Deck(2)
    print(f"Cards in two decks: {len(deck)}")
    print(f"Draw card: {deck.draw()}")
    print(f"Remaining cards after draw: {len(deck)}")