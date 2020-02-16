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
        
        if self.suit == None:
            score = self.value
        elif self.value in [2, 3, 4, 5, 6, 7, 8, 9, 10]:
            score = self.value
        elif self.value in ["J", "Q", "K"]:
            score = 10
        elif self.value == "A":
            # initialize A as 11 - flip it to a 1 later if the hand score is > 21
            score = 11

        self.score = score
    
    def __repr__(self):
        if self.suit == None:
            return f"Score: {self.score}"
        else:
            return f"{self.value}{self.suit}"

    def __add__(self, other):
        result = self.score + other.score
        return Card(result, None)


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
    def __init__(self, deck):
        self.hand = []
        self.hit(deck)
        self.hit(deck)

    def __repr__(self):
        print("\nPlayer Hand")
        for card in self.hand:
            print(card)
        print(f"Player Score: {self.score()}")
        return ""
    
    def hit(self, deck, hidden=False):
        # use pop method to remove card from deck and add to player hand attribute
        card = deck.draw()
        self.hand.append(card)
        
        if hidden:
            return ""
        else:
            return print(f"Card Drawn: {card}")

    def score(self):
        raw_score = sum(self.hand, Card(0, None))
        # need to keep track of aces to pick the best hand
        
        for card in self.hand:
            if raw_score.score > 21 and card.value == "A" and card.score == 11:
                card.score = 1
                raw_score = sum(self.hand, Card(0, None))
        
        score = raw_score.score

        return score

    def play(self):
        # show you your hand
        # ask if you want to hit
        # then score your hand
        # if hand score > 21 you lose
        # if no hit, player turn ends
        return "player play"


class Dealer(Player):
    def __init__(self, deck):
        self.hand = []
        self.hit(deck, hidden=True)
        self.hit(deck)

    def initial_hand(self):
        # show dealer's card with one card hidden
        return "show dealer hand"
    
    def play(self, deck):
        
        while self.score < 17:
            self.hit(deck)
        # flip over hidden card
        # play while hand is less than or equal to 16
        # if > 21, bust
        # if > 16 but less than player, player wins
        # else dealer wins

def setup_game():
    return "setup"

def play_game():
    return "play game"


if __name__ == "__main__":
    # code to test that specifying number of decks works correctly
    print("TEST 1")
    deck = Deck(1)
    print(f"Cards in one deck: {len(deck)}")
    deck = Deck(2)
    print(f"Cards in two decks: {len(deck)}")
    print("\n")

    # code to test that deck.draw() method works correctly
    print("TEST 1")
    deck = Deck(2)
    print(f"Cards in two decks: {len(deck)}")
    print(f"Draw card: {deck.draw()}")
    print(f"Remaining cards after draw: {len(deck)}")
    print("\n")

    # code to test create player and print player stats
    print("TEST 3")
    print("Creating player...")
    player = Player(deck)
    print(player)

    # code to test player hands with Aces
    print("TEST 4")
    deck = Deck(2)
    player = Player(deck)
    # Test all Aces must be of value 1
    player.hand = [Card("A", "D"), Card("A", "H"), Card("A", "C"), Card("J", "S")]
    print(player)
    
    deck = Deck(2)
    player = Player(deck)
    # Test all Aces must be of value 1
    player.hand = [Card("A", "D"), Card("A", "H"), Card("J", "S"), Card("J", "C")]
    print(player)
    
    deck = Deck(2)
    player = Player(deck)
    # Test Ace must be of value 11
    player.hand = [Card("A", "D"), Card(2, "H"), Card(10, "C"), Card(8, "C")]
    print(player)
    
    deck = Deck(2)
    player = Player(deck)
    # Test one Ace of value 11 and one Ace of value 1
    player.hand = [Card("A", "C"), Card("A", "H"), Card(3, "H"), Card(6, "C")]
    print(player)