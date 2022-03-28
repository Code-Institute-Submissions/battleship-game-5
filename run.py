"""
Import random go to generate random int in game
"""

from random import randint 

# Two Player one is user_name and another is Computer
user_name = raw_input("Please enter your name: ")
Computer_name = "Computer"

# user can create grid size self
grid_size = int(input("Please Enter your grid size: "))

# Declare variable user_board and computer_board
user_board = []
computer_board = []
user_guess_row = -1
user_guess_col = -1
computer_guess_row = -1
computer_guess_col = -1

# create for loop for grid size board
for x in range(grid_size):
    user_board.append([ '  .  '] * grid_size)

for x in range(grid_size):
    computer_board.append(['  .  '] * grid_size)

# define a function to show board and take two paramiter (board and name)
def print_board(board, name):
    print("--------------------------")
    print (name + "'s board")
    for row in board:
        print " ".join(row)

# create a function name random_num and parameter 'board' 
def random_num(board):
    return randint(0, len(board) - 1)

# create two variable computer_ship_row and computer_ship_col for computer board
computer_ship_row = random_num(computer_board)
computer_ship_col = random_num(computer_board)

# create two variable user_ship_row and user_ship_col for user board
user_ship_row = random_num(user_board)
user_ship_col = random_num(user_board)

user_board[user_ship_row] [user_ship_col] = "@"

# print user_board and computer_board and there name
print_board(user_board, user_name)
print_board(computer_board, computer_name)

# create a function take_input_and_play_game
def take_input_and_play_game():
    global user_guess_row, user_guess_col, computer_guess_row, computer_guess_col
    user_guess_row = int(raw_input("Guess a row: "))
    user_guess_col = int(raw_input("Guess a col: "))
    computer_guess_row = random_num(computer_board)
    computer_guess_col = random_num(computer_board)
    play_game()


