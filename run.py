# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high


"""
GAME EXPLANATION
    The computer will generate 5 ships on a board and 
    and then the player'll guess where those 5 ships are located.

The player has one board GUESS_BOARD, where he will make his the guesses. 
The other board HIDDEN_BOARD is where the computer 
will generate randomly 5 ships, each in one cell.

This is one player game, and it will have only
two boards.
"""
# Legend
# 'X' for placing battleship and hit battleship
# ' ' for available space
# '-' for missed shot

from random import randint

HIDDEN_BOARD = [[' '] * 8 for x in range(8)]
"""
This board holds our ships
"""
GUESS_BOARD = [[' '] * 8 for x in range(8)]
"""
This board holds enemy ships
"""
lsns = {'A': 0, 'B' : 1, 'C' : 2, 'D' : 3, 'E' : 4, 'F' : 5, 'G' : 6, 'H' : 7}
"""
Convert letters to numbers
"""
def print_board(board):
    #print first column which is the header
    print("  A B C D E F G H")
    print('  ---------------')
    row_number = 1
    # initializer
    #%d for decimal, %s for string
    #% means format
    for row in board:
        print("%d|%s|" % (row_number, "|".join(row)))  
    # for each row we are iterating we join the pipe as seperator
        row_number += 1
"""
Starting the game by creating ships randomly
"""
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
    while True: 
        try: 
            # Asks the user what row and what column the ship is 
            row = input('Please enter a ship row 1-8: ') 
            while row not in set('12345678') or row == "": 
                print("Please enter a valid row") 
                row = input('Please enter a ship row 1-8: ') 
            column = input("Please enter a ship column A-H: ").upper() 
            
            while column not in set('ABCDEFGH') or column == "": 
                print("Please enter a valid column") 
                column = input("Please enter a ship column A-H: ").upper() 
            # Use a dictionary to map columns to indexes 
            column_index_map = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7} 
            return int(row) - 1, column_index_map[column] 
        except ValueError as ve: 
            print(f"A ValueError occurred: {ve}. Please try again.")
        except KeyError: 
            print("Please enter a valid column letter from A to H.")
        except Exception as ex: 
            print(f"An unexpected error occurred: {ex}. Please try again.")
 


def count_hit_ships(board):
    # Checking if the ship exists
    # Goes through each row and each column
    # If we hit all five the game is over
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
    
