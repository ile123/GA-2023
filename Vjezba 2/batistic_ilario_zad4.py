import random

game_rules = {
    ("rock", "rock"): "DRAW",
    ("paper", "paper"): "DRAW",
    ("scissors", "scissors"): "DRAW",
    ("rock", "scissors"): "PLAYER WON",
    ("paper", "rock"): "PLAYER WON",
    ("scissors", "paper"): "PLAYER WON",
    ("rock", "paper"): "COMPUTER WON",
    ("paper", "scissors"): "COMPUTER WON",
    ("scissors", "rock"): "COMPUTER WON",
}

actions = ["rock", "paper", "scissors"]

def play_game():
    print("\n########################################## PLAYING THE GAME NOW ##########################################")
    computer_choice = actions[random.randint(0, 2)]
    choice = int(input("\n1.) Rock\n2.) Paper\n3.) Scissors\n\n"))
    if choice == 1:
        choice = "rock"
    elif choice == 2:
        choice = "paper"
    elif choice == 3:
        choice = "scissors"
    else:
        print("ERROR: WRONG INPUT, THE INPUT HAS TO BE FROM 1-3")
        return
    print(f"ROUND OUTCOME: {game_rules[(choice, computer_choice)]}")
    print("\n########################################## END OF THE GAME ##########################################")


def function_4():
    print("\n########################################## ROCK, PAPER, SCISSORS ##########################################")
    while True:
        choice = int(input("\n1.) Play\n2.) Exit\n\n"))
        if choice == 1:
            play_game()
        elif choice == 2:
            print("\n########################################## END OF PROGRAM ##########################################")
            break
        else:
            print("WRONG INPUT(IT HAS TO BE EITHER 1 OR 2")