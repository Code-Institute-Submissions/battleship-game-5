from random import randint

"""
Import random go to generate random int in game.
"""

print("----------------------------- \n Wellcome to ULTIMATE BATTLESHIP! \n "
      "Board size player can decide. \n top left corner is raw: 0, col: 0 "
      "\n ----------------------------- ")
user_name = input("Please enter your name: ")
computer_name = "Computer"

grid_size = int(input("Please enter grid size: "))

user_board = []
computer_board = []
user_guess_row = -1
user_guess_col = -1
com_guess_row = -1
com_guess_col = -1

for x in range(grid_size):
    user_board.append(['  .  '] * grid_size)

for x in range(grid_size):
    computer_board.append(['  .  '] * grid_size)


def print_board(board, name):
    print("-------------------------------")
    print(name + "'s board")
    for row in board:
        print(" ".join(row))


def random_num(board):
    return randint(0, len(board) - 1)


com_ship_row = random_num(computer_board)
com_ship_col = random_num(computer_board)

user_ship_row = random_num(user_board)
user_ship_col = random_num(user_board)

user_board[user_ship_row][user_ship_col] = "@"

print_board(user_board, user_name)
print_board(computer_board, computer_name)


def take_input_and_play_game():
    global user_guess_row
    global user_guess_col
    global com_guess_row
    global com_guess_col

    user_guess_row = int(input("Guess a row: "))
    user_guess_col = int(input("Guess a col: "))
    com_guess_row = random_num(computer_board)
    com_guess_col = random_num(computer_board)
    play_game()


def play_game():
    if ((user_guess_row < 0 or user_guess_row > grid_size) or
            (user_guess_col < 0 or user_guess_col > grid_size)):
        print("Oops, that's not even in the ocean. Guess again:")
        take_input_and_play_game()
    else:
        show_result()


def show_result():
    my_guess = str(user_guess_row) + "," + str(user_guess_col)
    print("Player guessed: (" + my_guess + ")")
    if (user_guess_row == com_ship_row and
            user_guess_col == com_ship_col):
        print("Congratulations!" + user_name + "win")
    else:
        print(user_name + " missed this time.")

        computer_guess = str(com_guess_row) + "," + str(user_guess_col)
        print("Computer guessed: (" + computer_guess + ")")

        if (com_guess_row == com_ship_row and
                com_guess_col == com_ship_col):
            print("Congratulations! computer win")
        else:
            print("Computer missed this time.")
    return show_result


take_input_and_play_game()
