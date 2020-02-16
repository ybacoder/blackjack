import blackjack

play = "y"

num_decks = int(
    input("How many decks would you like to play with? Enter integer (1-9): ")
)
while num_decks not in range(1, 10):
    print("Invalid entry. Try again.")
    num_decks = int(
        input("How many decks would you like to play with? Enter integer (1-9): ")
    )

while play in ["y", "Y"]:
    print(blackjack.play_game(num_decks))

    play = input("-" * 50 + "\nWould you like to play again? y/n ")
    while play not in ["y", "Y", "n", "N"]:
        print("Invalid entry. Try again.")
        play = input("\nWould you like to play again? y/n ")

    if play in ["n", "N"]:
        break
