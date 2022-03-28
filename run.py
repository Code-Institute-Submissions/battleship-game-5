"""
Import random go to generate random int in game.
"""
from random import randint

user_name = raw_input("Please enter your name: ")
computer_name = "Computer"

grid_size = int(input("Please enter grid size: "))

user_board = []
computer_board = []
user_guess_row = -1
user_guess_col = -1
computer_guess_row = -1
computer_guess_col = -1

for x in range(grid_size):
    user_board.append(['  .  '] * grid_size)

for x in range(grid_size):
    computer_board.append(['  .  '] * grid_size)


def print_board(board, name):
    print ("-------------------------------")
    print (name + "'s board")
    for row in board:
        print (" ".join(row))


def random_num(board):
    return randint(0, len(board) - 1)


computer_ship_row = random_num(computer_board)
computer_ship_col = random_num(computer_board)

user_ship_row = random_num(user_board)
user_ship_col = random_num(user_board)

user_board[user_ship_row][user_ship_col] = "@"

print_board(user_board, user_name)
print_board(computer_board, computer_name)


def take_input_and_play_game():
    global user_guess_row, user_guess_col, computer_guess_row, computer_guess_col
    user_guess_row = int(raw_input("Guess a row: "))
    user_guess_col = int(raw_input("Guess a col: "))
    computer_guess_row = random_num(computer_board)
    computer_guess_col = random_num(computer_board)
    play_game()


def play_game():
    if (user_guess_row < 0 or user_guess_row > grid_size) or (user_guess_col < 0 or user_guess_col > grid_size):
        print ("Oops, that's not even in the ocean. Guess again:")
        take_input_and_play_game()
    else:
        show_result()


def show_result():
    print ("Player guessed: (" + str(user_guess_row) + "," + str(user_guess_col) + ")")
    if user_guess_row == computer_ship_row and user_guess_col == computer_ship_col:
        print ("Congratulations!" + user_name + "win")
    else:
        print (user_name + " missed this time.")

    print ("Computer guessed: (" + str(computer_guess_row) + "," + str(user_guess_col) + ")")
    if computer_guess_row == computer_ship_row and computer_guess_col == computer_ship_col:
        print ("Congratulations!" + "computer win")
    else:
        print "Computer missed this time."

take_input_and_play_game()
