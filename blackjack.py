"""
Yacub Bholat
Data Analysis and Visualization Boot Camp
Blackjack Homework (Optional)
Due: 23 February 2020
"""

import random as r
import time
sleep_time = 0.4

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
        print(f"{self.__class__.__name__} Hand:", end=" ")
        
        if self.__class__.__name__ == "Player":
            hidden = False
        else:
            hidden = True

        self.hand = []
        
        self.hit(deck, hidden)
        self.hit(deck)
        
        print("")
        if self.__class__.__name__ == "Player":
            print(f"Player Score: {self.score()}")
        print("")

    def __repr__(self):
        print(f"\n{self.__class__.__name__} Hand:", end=" ")
        for card in self.hand:
            print(card, end=" ")
        print(f"\n{self.__class__.__name__} Score: {self.score()}")
        return ""
    
    def hit(self, deck, hidden=False):
        # use pop method to remove card from deck and add to player hand attribute
        card = deck.draw()
        self.hand.append(card)
        
        if hidden:
            return print("xx", end=" ")
        else:
            return print(card, end=" ")

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
    def play(self, deck):
        while self.score() < 17:
            time.sleep(sleep_time)
            print("Dealer draws: ", end="")
            self.hit(deck)
            print(self)
        # flip over hidden card
        # play while hand is less than or equal to 16
        # if > 21, bust
        # if > 16 but less than player, player wins
        # else dealer wins

def setup_game(num_decks):
    deck = Deck(num_decks)
    dealer = Dealer(deck)
    player = Player(deck)
    return deck, dealer, player

def play_game(num_decks):
    print("Welcome to Blackjack!")
    print("Get as close to 21 as possible.\n")
    deck, dealer, player = setup_game(num_decks)
    
    while player.score() <= 21:
        hit = input("Would you like to hit? y/n ")
        if hit in ["n", "N"]:
            break
        elif hit in ["y", "Y"]:
            print("Player draws: ", end="")
            player.hit(deck)
            print(player)
        else:
            print("Invalid entry. Try again.")
    if player.score() > 21:
        game_result = "PLAYER BUSTS, DEALER WINS!"
    else:
        time.sleep(sleep_time)
        print(dealer)
        dealer.play(deck)
        if dealer.score() > 21:
            game_result = "DEALER BUSTS, PLAYER WINS!"
        elif dealer.score() >= player.score():
            game_result = "DEALER WINS!"
        else:
            game_result = "PLAYER WINS!"
    return game_result


if __name__ == "__main__":
    # code to test that specifying number of decks works correctly
    print("TEST 1")
    deck = Deck(1)
    print(f"Cards in one deck: {len(deck)}")
    deck = Deck(2)
    print(f"Cards in two decks: {len(deck)}")
    print("\n")

    # code to test that deck.draw() method works correctly
    print("TEST 2")
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
    # Test all Aces must be of value 1
    player.hand = [Card("A", "D"), Card("A", "H"), Card("A", "C"), Card("J", "S")]
    print(player)
    
    # Test all Aces must be of value 1
    player.hand = [Card("A", "D"), Card("A", "H"), Card("J", "S"), Card("J", "C")]
    print(player)
    
    # Test Ace must be of value 11
    player.hand = [Card("A", "D"), Card(2, "H"), Card(10, "C"), Card(8, "C")]
    print(player)
    
    # Test one Ace of value 11 and one Ace of value 1
    player.hand = [Card("A", "C"), Card("A", "H"), Card(3, "H"), Card(6, "C")]
    print(player)

    # code to test dealer creation
    print("TEST 5")
    dealer = Dealer(deck)
    print(dealer)

    # code to test game setup
    print("TEST 6")
    setup_game(2)

    # code to test gameplay
    print("\n\nTEST 7")
    print(play_game(2))