### Introduction (Game Explanation)

This is one player game, and it has only
two boards. The computer generates five ships on the HIDDEN_BOARD
and the player guesses ships location on the GUESS_BOARD. Each ships takes 
only one cell. Only the GUESS_BOARD is visible to the player. After ten
turns the game is over.

The player has one board GUESS_BOARD, where he will make his guesses. 
The hit ship will be marked with X on the GUESS_BOARD (Player's board).
The miss will be marked with hifen -
The other board HIDDEN_BOARD is where the computer 
will generate randomly 5 ships, each in one cell.

This is a one player game.

Screenshot for responsive design.

 ![The game!](outline.png "The outline from ami.responsivedesign")


 ### Welcome to the Battleship game!

 Please click on the link below to open the application.
 
 [Battleship](https://battle-d964f125f218.herokuapp.com/)

### Features

This application is for entertainment.

 + The program accepts user inputs, maintains scores, validates the inputs.
 + Coordinates outside of the board can not be entered.
 + Player must enter row number and column letter.

### Future Features

 + Have ships larger than one cell
 + Allow player to select the board size, number of ships and ship sizes.

 ### Flow chart to work out the logic path the program needs to take 


 ![The SCHEME!](scheme.jpg "CHART")




 ### Bugs

 The application had one bug. Namely the row iteration was not working. Instead of showing 1,2,3,4,5,6,7,8 it showed only 1,1,1,1,1,1,1,1.
 By clearing an empty space the bug was resolved.

 ![The row iteration bug!](bug_rows.png "The bug")


 This game was taken from youtube channel of Knowledge Mavens.
 There is a bug in this code, which appears if the player does not put anything for row or column.
 In that case the program crashes.

 ![The empty space bug!](bug.png "The bug")

 If tha player hits enter without typing anything the program crashes. I tried to resolved by
 using 
 Try:
Except KeyValue:
Probably it could work, but I couldn't make it. I solved this problem by adding some code.

This is in the section, function get_ship_location. Namely within the while loop which loops as many times as the user puts wrong letters or numbers, the program promts the user to enter valid number and letter. However if the user presses enter without entering anything the program crashes. 

The code is as follows:  
    while row not in '12345678':
        print("Please enter a valid row")
        row = input('Please enter a ship row 1-8: ')
    crashes when the gamer just preses enter.

    My contribution is modifying the code as follows.
    while row not in '12345678' or row in " " :
        print("Please enter a valid row")
        row = input('Please enter a ship row 1-8: ')

        Adding 
        or row in " ":
    This prevents the program from crashing.

It turned out that the program crashes if the user puts two consecutive numbers or letters. This problem is solved with additional improvement of the control flow by putting set in front of the string set('12345678'), since turning the string into a set(or a list or a tuple) will break it into individual characters. This idea was accepted from stackoverflow.com

      The code is as follows:  
      while row not in set('12345678') or " ":
         print("Please enter a valid row")
         row = input('Please enter a ship row 1-8: ')
    The program doesn't crash when the user puts 12 or AC etc.

Here is the screenshot showing the bug fix.

![The two numbers two letters bug!](two_letter_bug.png "The two letter/figure bug")

All the control flow was taken out. Try and Except KeyError message added as follows:
  
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
            column_index_map = {
                            'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7
                               }
            return int(row) - 1, column_index_map[column]
        except ValueError as ve:
            print(f"A ValueError occurred: {ve}. Please try again.")
        except KeyError:
            print("Please enter a valid column letter from A to H.")
        except Exception as ex:
            print(f"An unexpected error occurred: {ex}. Please try again.")

  The program does not break, and usually doesn't show the KeyError message. The message from the while block is displayed.

![The no except message bug!](no_except_mess.png "The no exceptio message bug")

Here is an example when the program throws except message. ValueError occured: invalid literal for int() with base 10: 'd' Please try again. Note that the first line is l not 1.

![This shows that the try except block works.!](try_except_error.png "The no exceptio message bug")


It is explained in the Game Explanation only the guess board is visible. So the code was updated so that the hidden board to be displayed only if the gamer wants to do that.
![This shows the hidden board. The old version!](hidden.png "The hidden board is shown")

The code was updated with the option the hidden board to be displayed only if the gamer wants to.

![This shows the hidden board. The new version!](hidden_two.png "The hidden board is shown at the will of the gamer.")

This is achieved with the creation of new function

   def reveal_hidden_board():
   
       """
       Prints the hidden board for the player to view.
       """
    print("HIDDEN BOARD:")
    print_board(HIDDEN_BOARD)

    view_hidden = input(
        "Would you like to view the hidden board? (yes/no): "
        ).strip().lower()
    if view_hidden == 'yes':
        reveal_hidden_board()
  

## Testing

The testing was made on Code Institute CI Python Linter.

![The image from CI python linter!](CI_Python_Linter.png "CHART")

There are no errors as shown on the screenshot.

### Programs and software used for creating this project

The language that was used is Python3 and Git Bash, Visual Studio Code.
Git Bash is an application that interfaces with the operating system
through written commands.

This is a Command Line Application.

 This application is dynamic and is deployed on HEROKU server.

 GitHub was used to store the project's code, after being pushed
 from Git.

 Git was used by utilizing the Gitpod terminal to commit to Git and push to GitHub.

 Several python functions were used:

  + print_board
  + create_ships
  + get_ship_location
  + count_hit_ships
    + while loop is used in the function for validation
  + reveal_hidden_board

## Deployment

The Visual Studio Code was used to create this application.

git add . was  used to add the files to the staging area

  git commit -m "Commit message"
This command was used to commit changes to the local repository queue
ready for the final step

  git push - This command was used to push all the committed code to the remote repository
on git hub

The game was deployed on the Heroku platform, thus making it accessible to the users.

First the application was deployed by codeanywhere.com, and after that I was unable to
make additional changes and to reach my deployed application using codeanywhere anymore. The additional
changes like fixing the bugs, making additional commits and creating this file README.md were made 
from my local repository, which was cloned from GitHub, to my desktop and using Visual Studio Code and the Command Line Interface (CLI), Git Bash commands namely 

      git remote add heroku https://git.heroku.com/app.git
      git push heroku master
      
This happens only after login from Git Bash
   
      `heroku login`

which displayed the CLI authentication token.
For this to happen HEROKU CLI had to be installed and then upgraded to to version 8.9.0
namely by using
      sudo apt -get update && sudo apt -get update heroku

## Forking on GitHub

- To create a personal copy of a public repository to contribute to a project go to GitHub repository to fork.

    Make changes to the code, add features, fix issues or modify code within your fork, 
    make changes that dont affect the original repository. If you want to send your changes
    back to the owner, you can do so by creating a "Pull Request".

## Credits

Special thanks to my mentor Medale Oluwafemi for helping me creating this README.md file, to Marco from the techical issues,and cohort facilitator Laura from Codeinstitute. The idea was taken from youtube channel of Knowledge Mavens and improved with try except block.











