"""
tic_tac_toe.py: Druhý projekt do Engeto Online Python Akademie

author: Patrik Novotny
email: novotpat@gmail.com
discord: PatrikN#7617
"""
import os

from game_rules import Text

# Welcome to player/s, introducing the game rules and show the playground
print("Welcome to Tic Tac Toe", "=" * 41,"".join(Text), "=" * 41,sep="\n")
print("Let's start the game", "-" * 41,sep="\n")

def game():

    # The playground
    board = {"7": "   ", "8": "   ", "9": "   ",
             "4": "   ", "5": "   ", "6": "   ",
             "1": "   ", "2": "   ", "3": "   "}
    running_game = True
    turn = "X"
    count = 0

    def grid():
        print("+---" * 3 + "+")
        print(f"|{board ['7']: ^3}|{board ['8']: ^3}|{board ['9']: ^3}|")
        print("+---" * 3 + "+")
        print(f"|{board ['4']: ^3}|{board ['5']: ^3}|{board ['6']: ^3}|")
        print("+---" * 3 + "+")
        print(f"|{board ['1']: ^3}|{board ['2']: ^3}|{board ['3']: ^3}|")
        print("+---" * 3 + "+")

    grid()

    while running_game:
        print("=" * 41)
        move = input(f"Player {turn} | Please enter your move number: ")
        print("=" * 41)
        if not move.isnumeric():
            print("Input is not a number....")
            continue
        elif int(move) not in range(1, 10):
            print("The number is not in the range....")
            continue
        elif board[move] != "   ":
            print("Entered number is occupied...")
            continue
        else:
            os.system("cls")
            board[move] = turn
            count += 1
            grid()

        # Evaluation of the game
        if count >= 5:
            if board["7"] == board["8"] == board["9"] != "   ":  # top row
                print(f"Congratulations, the player {turn} WON! ")
                running_game = False
            elif board["4"] == board["5"] == board["6"] != "   ":    # middle row
                print(f"Congratulations, the player {turn} WON! ")
                running_game = False
            elif board["1"] == board["2"] == board["3"] != "   ":    # bottom row
                print(f"Congratulations, the player {turn} WON! ")
                running_game = False
            elif board["1"] == board["4"] == board["7"] != "   ":    # left column
                print(f"Congratulations, the player {turn} WON! ")
                running_game = False
            elif board["2"] == board["5"] == board["8"] != "   ":    # middle column
                print(f"Congratulations, the player {turn} WON! ")
                running_game = False
            elif board["3"] == board["6"] == board["9"] != "   ":    # right column
                print(f"Congratulations, the player {turn} WON! ")
                running_game = False
            elif board["1"] == board["5"] == board["9"] != "   ":    # first diagonal
                print(f"Congratulations, the player {turn} WON! ")
                running_game = False
            elif board["3"] == board["5"] == board["7"] != "   ":    # second diagonal
                print(f"Congratulations, the player {turn} WON! ")
                running_game = False
            else:
                if count == 9:
                    print("It's a Tie")
                    running_game = False

        # Players switching
        if turn == "X":
            turn = "O"
        else:
            turn = "X"

game()

# Next game
while (next_game := input("\nDo you want to play a next game? 'y/n': ")) == "y":
    game()


