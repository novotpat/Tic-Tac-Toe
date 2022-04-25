"""
tic_tac_toe.py: Druhý projekt do Engeto Online Python Akademie

author: Patrik Novotny
email: novotpat@gmail.com
discord: PatrikN#7617
"""
import pprint

from game_rules import Text
from grid import grid

# Welcome to player/s, introducing the game rules and show the playground
print("Welcome to Tic Tac Toe", "=" * 41,"".join(Text), "=" * 41,sep="\n")
print("Let's start the game", "-" * 41,sep="\n")
print("".join(grid))
