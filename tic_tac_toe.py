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

# The playground
board = {"7": "   ", "8": "   ", "9": "   ",
             "4": "   ", "5": "   ", "6": "   ",
             "1": "   ", "2": "   ", "3": "   "}

def grid():
    print("+---" * 3 + "+")
    print(f"|{board ['7']: ^3}|{board ['8']: ^3}|{board ['9']: ^3}|")
    print("+---" * 3 + "+")
    print(f"|{board ['4']: ^3}|{board ['5']: ^3}|{board ['6']: ^3}|")
    print("+---" * 3 + "+")
    print(f"|{board ['1']: ^3}|{board ['2']: ^3}|{board ['3']: ^3}|")
    print("+---" * 3 + "+")
grid()

def game():
    running_game = True
    turn = "X"
    count = 0
    while running_game:
        print("=" * 41)
        move = input(f"Player {turn} | Please enter your move number: ")
        print("=" * 41)
        if not move.isnumeric():
            print("Input is not a number....")
        elif int(move) not in range(1, 10):
            print("The number is not in the range....")
        elif board[move] != "   ":
            print("Entered number is occupied...")
        else:
            board[move] = turn
            count += 1
            grid()
        # Evaluation of the game
        if count >= 5:
            if board["7"] ==  board["8"] == board["9"] != "   ":  # top row
                running_game = False
                print(f"Congratulations, the player {turn} WON! ")
            elif board["4"] ==  board["5"] == board["6"] != "   ":    # middle row
                running_game = False
                print(f"Congratulations, the player {turn} WON! ")
            elif board["1"] ==  board["2"] == board["3"] != "   ":    # bottom row
                running_game = False
                print(f"Congratulations, the player {turn} WON! ")
            elif board["1"] ==  board["4"] == board["7"] != "   ":    # left column
                running_game = False
                print(f"Congratulations, the player {turn} WON! ")
            elif board["2"] ==  board["5"] == board["8"] != "   ":    # middle column
                running_game = False
                print(f"Congratulations, the player {turn} WON! ")
            elif board["3"] ==  board["6"] == board["9"] != "   ":    # right column
                running_game = False
                print(f"Congratulations, the player {turn} WON! ")
            elif board["1"] ==  board["5"] == board["9"] != "   ":    # first diagonal
                running_game = False
                print(f"Congratulations, the player {turn} WON! ")
            elif board["3"] ==  board["5"] == board["7"] != "   ":    # second diagonal
                running_game = False
                print(f"Congratulations, the player {turn} WON! ")
        if count == 9:
            running_game = False
            print("It's a Tie")
        # Players switching
        if turn == "X":
            turn = "O"
        else:
            turn = "X"
    else:
        running_game = False

game()

