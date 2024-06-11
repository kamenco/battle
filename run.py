from random import randint

# Initialize the boards
HIDDEN_BOARD = [[' '] * 8 for _ in range(8)]
GUESS_BOARD = [[' '] * 8 for _ in range(8)]

# Mapping from letters to numbers
letters_to_numbers = {
    'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}


def print_board(board):
    """
    Prints the board in a readable format.
    """
    print("  A B C D E F G H")
    print('  ---------------')
    row_number = 1
    for row in board:
        print(f"{row_number}|{'|'.join(row)}|")
        row_number += 1


def create_ships(board):
    """
    Randomly places 5 ships on the board.
    """
    for _ in range(5):
        ship_row, ship_column = randint(0, 7), randint(0, 7)
        while board[ship_row][ship_column] == 'X':
            ship_row, ship_column = randint(0, 7), randint(0, 7)
        board[ship_row][ship_column] = 'X'


def get_ship_location():
    """
    Prompts the player to enter a guess for the ship location.
    Returns a tuple of (row, column).
    """
    while True:
        try:
            row = input('Please enter a ship row 1-8: ')
            if len(row) == 1 and row in '12345678':
                row = int(row) - 1
            else:
                print("Please enter a valid row between 1 and 8.")
                continue
            column = input("Please enter a ship column A-H: ").upper()
            if len(column) == 1 and column in 'ABCDEFGH':
                column = letters_to_numbers[column]
            else:
                print("You have entered invalid column. Please start anew.")
                continue
            return row, column
        except Exception as ex:
            print(f"An error occurred: {ex}. Please try again.")


def count_hit_ships(board):
    """
    Counts the number of ships hit on the board.
    """
    return sum(row.count('X') for row in board)


def reveal_hidden_board():
    """
    Prints the hidden board for the player to view.
    """
    print("HIDDEN BOARD:")
    print_board(HIDDEN_BOARD)

# Main game logic


create_ships(HIDDEN_BOARD)
turns = 10

print('Welcome to Battleship')
while turns > 0:
    print_board(GUESS_BOARD)
    row, column = get_ship_location()
    if GUESS_BOARD[row][column] in ['-', 'X']:
        print("You already guessed that")
    elif HIDDEN_BOARD[row][column] == 'X':
        print("Congratulations, you have hit a battleship")
        GUESS_BOARD[row][column] = 'X'
    else:
        print('Sorry, you missed')
        GUESS_BOARD[row][column] = '-'
    turns -= 1
    if count_hit_ships(GUESS_BOARD) == 5:
        print("Congratulations, you have sunk all the battleships.")
        break
    print(f'You have {turns} turns remaining')
    # Ask if the player wants to see the hidden board
    view_hidden = input(
        "Would you like to view the hidden board? (yes/no): "
        ).strip().lower()
    if view_hidden == 'yes':
        reveal_hidden_board()

if turns == 0:
    print('Sorry, you ran out of turns, the game is over')
    print_board(HIDDEN_BOARD)  # Reveal the hidden board at the end of the game
