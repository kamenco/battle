def get_ship_location(): 
    while True: 
        try: 
            # Asks the user what row and what column the ship is 
            row = input('Please enter a ship row 1-8: ') 
        while row not in set('12345678') or row.strip() == "": 
            print("Please enter a valid row") 
            row = input('Please enter a ship row 1-8: ') 
            column = input("Please enter a ship column A-H: ").upper() 
        while column not in set('ABCDEFGH') or column.strip() == "": 
            print("Please enter a valid column") 
            column = input("Please enter a ship column A-H: ").upper() 
            # Use a dictionary to map columns to indexes 
            column_index_map = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7} 
            return int(row) - 1, column_index_map[column] 
        except ValueError as ve: print(f"A ValueError occurred: {ve}. Please try again.")
        except KeyError: print("Please enter a valid column letter from A to H.")
        except Exception as ex: print(f"An unexpected error occurred: {ex}. Please try again.")
 
AI T