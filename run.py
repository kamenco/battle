# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

# Legend
# 'X' for placing battleship and hit battleship
# ' ' for available space
# ' ' for missed shot



from random import randint

HIDDEN_BOARD = [[' '] * 8 for x in range(8)]
"""
This board holds our ships
"""
GUESS_BOARD = [[' '] * 8 for x in range(8)]
"""
This board holds enemy ships
"""

letters_to_numbers = {'A': 0, 'B' : 1, 'C' : 2, 'D' : 3, 'E' : 4, 'F' : 5, 'G' : 6, 'H' : 7}
"""
Convert letters to numbers
"""
def print_board(board):
    print("  A B C D E F G H")
    print('  ----------------')
    row_number = 1
    # initializer
    for row in board:
        print("%d|%s|" % (row_number, "|".join(row)))
    
    # for each row we are iterating we join the pipe as seperator
    
    row_number += 1

def create_ships(board):
    
    # Generates shipds randomly
    
    for ship in range(5):
        ship_row, ship_column = randint(0, 7), randint(0, 7)
        while board[ship_row] [ship_column] == 'X':
    # check if 'X' exists
            ship_row, ship_column = randint(0, 7), randint(0, 7)
        board [ship_row][ship_column] = 'X'

    # set it to 'X'

def get_ship_location():
    
    
    # Asks the user what row and what column the ship is
     
    row = input('Please enter a ship row 1-8: ')
    while row not in '12345678':
        print("Please enter a valid row")
        row = input('Please enter a ship row 1-8: ')
    column = input("Please ente a ship column A-H: ").upper()
    while column not in 'ABCDEFGH':
        print("Please enter a valid column")
        column = input("Please ente a ship column A-H: ").upper()
    return int(row) - 1, letters_to_numbers[column]
    # Wrap this in try and except because if user doesnt put anything
    # the program will crash 


def count_hit_ships(board):
    # Checking if the ship exists
    # Goes through each row and each column
    count = 0
    for row in board:
        for column in row:
            if column == 'X':
                count += 1
    return count

create_ships(HIDDEN_BOARD)
print_board(HIDDEN_BOARD)
turns = 10
while turns > 0:
    print('Welcome to battleship')
    print_board(GUESS_BOARD)
    row, column = get_ship_location()
    if GUESS_BOARD[row][column] == '-':
        print("You already guessed that")
    elif HIDDEN_BOARD[row][column] == 'X':
        print("Congratulation, you have hit a battleship")
        GUESS_BOARD[row][column] = 'X'
        turns -= 1
    else:
        print('Sorry, you missed')
        GUESS_BOARD[row][column] = '-'
        turns -= 1
    if count_hit_ships(GUESS_BOARD) == 5:
        print("Congratulations, you have sunk all the battleships.")
        break
    print('You have ' + str(turns) + ' turns remaining')
    if turns == 0:
        print('Sorry, you ran out of terms, the game is over')
        break