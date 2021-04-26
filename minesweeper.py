#imports built in random file to provide random integers
import random

#imports built in os file to provide a way convenient way to clear the terminal
import os



#function that sets the size of the playing field
def field_size():

    #Initializes rows and columns at zero
    rows = 0
    cols = 0

    #asks the user to choose a playing field size and gives an option to customize the rows and columns
    field = input("\n\nChoose your playing field size. (1 = 8x8, 2 = 12x12, 3 = 16x16, or c = customize)... ")

    #if user opts to quit the game
    if field.lower() == "q":

        #provides a cancel option if the user accidentally entered q
        qut = input("\n\nAre you sure you want to quit? (y/n)... ")

        #upper or lower case 'y' will confirm quit
        if qut.lower() == "y":

            #prints goodbye and exits the game
            print("\nGoodbye!")
            quit()

        #if user backs out of quitting, the function is restarted
        else:
            return field_size()

    #if user enters 1
    if field == "1":

        #shows the user what they chose
        print("You chose an 8x8 playing field.")

        #resets the amount of rows and columns to 8
        rows = 8
        cols = 8

    #if user enters 2
    elif field == "2":

        #shows the user what they chose
        print("You chose a 12x12 playing field.")

        #resets the amount of rows and columns to 12
        rows = 12
        cols = 12

    #if user enters 3
    elif field == "3":

        #shows the user what they chose
        print("You chose a 16x16 playing field.")

        #resets the amount of rows and columns to 16
        rows = 16
        cols = 16

    #if the user chose to customize rows and columns
    elif field.lower() == "c":
        
        #loops until the chosen amount of rows fall in range 6-24
        #6 was chosen, because 5 cells deep seemed to small
        #24 was chosen, because 25 wide didn't fit on my screen, so I deemed 24x24 to be largest possible selection
        while rows < 6 or rows > 24:

            #asks user how many rows
            rows_str = input("\n\nHow many rows would you like in your field? (Choose a number between 5 and 25)... ")

            #if user opts to quit the game
            if rows_str.lower() == "q":

                #provides a cancel option if the user accidentally entered q
                qut = input("\n\nAre you sure you want to quit? (y/n)... ")

                #upper or lower case 'y' will confirm quit
                if qut.lower() == "y":

                    #print goodbye and exit the game
                    print("\nGoodbye!")
                    quit()

                #if user backs out of quitting the function is restarted
                else:
                    return field_size()

            #makes sure input can be converted to an integer
            try:
                rows = int(rows_str)

            #if input can't be converted to an integer, print instructive message and run back through the loop
            except:
                print("\n\nPlease enter a number between 5 and 25")

            
        #loops until the chosen amount of columns fall in range 6-24
        #6 was chosen, because 5 cells wide seemed to small
        #24 was chosen, because 25 wide didn't fit on my screen   
        while cols < 6 or cols > 24:

            #asks user how many columns
            cols_str = input("\n\nHow many columns would you like in your field? (Choose a number between 5 and 25)... ")

            #if user opts to quit the game
            if cols_str.lower() == "q":

                #provides a cancel option if the user accidentally entered q
                qut = input("\n\nAre you sure you want to quit? (y/n)... ")

                #upper or lower case 'y' will confirm quit
                if qut.lower() == "y":

                    #prints goodbye and exits the game
                    print("\nGoodbye!")
                    quit()

                #if user backs out of quitting, the function is restarted
                else:
                    return field_size()

            #makes sure input can be converted to an integer
            try:
                cols = int(cols_str)

            #if input can't be converted to an integer, prints instructive message and runs back through the loop
            except:
                print("\n\nPlease enter a number between 5 and 25")
        
        #shows the user what they chose
        print("You chose a {}x{} playing field.".format(rows, cols))

    #if the user entered anything other than the displayed characters, then prints an instructive message and restarts the function
    else:
        print("\n\nPlease choose 1, 2, 3, or 'c'.")
        return field_size()

    #function returns selected rows and columns
    return rows, cols



#function that determines the game difficulty
def difficulty():

    #asks user to choose a difficulty
    diff = input("\nChoose a difficulty (e = easy, m = med, h = hard)... ")

    #if user opts to quit the game
    if diff.lower() == "q":

        #provides a cancel option if the user accidentally entered q
        qut = input("\n\nAre you sure you want to quit? (y/n)... ")

        #upper or lower case 'y' will confirm quit
        if qut.lower() == "y":

            #prints goodbye and exits the game
            print("\nGoodbye!")
            quit()

        #if user backs out of quitting the function is restarted
        else:
            return difficulty()

    #if user chooses easy, mines will make up 15% of the total amount of cells
    if diff.lower() == "e":
        mines_perc = .15

    #if user chooses medium, mines will make up 20% of the total amount of cells
    elif diff.lower() == "m":
        mines_perc = .2

    #if user chooses hard, mines will make up 25% of the total amount of cells
    elif diff.lower() == "h":
        mines_perc = .25

    #if input was anything other than e m or h, then print instructive message and restart the function
    else:
        print("\n\nPlease enter 'e', 'm', or 'h'.")
        return difficulty()

    #returns the percentage of mines as a float
    return mines_perc



#function that prints the playing field when called. mines_left is the only value that fluctuates depending on when the function is called
def print_field(mines_left):

    #provides the global values needed in the function
    global rows
    global cols
    global shown_values

    #declares spacing variables that can be repeated to construct the playing field
    stu = "_____|"
    stv = "     |"

    #centers the game title over the field
    title_spacing = " " * int(((cols * 6) / 2) - 6)
    print("\n\n\n\t" + title_spacing + "Minesweeper\n\n")

    #begins column numbers at desired space that can be added to a repeating variable later
    show_col_nos = "      "

    #loops through column numbers
    for col in range(1, cols + 1):

        #if columns are single digit, gives an extra space to center fit over each column
        if col < 10:

            #adds the column to the string of columns
            show_col_nos += "     " + str(col)

        #if columns are double digit, removes a space to center fit over each column
        else:

            #adds the column to the string of columns
            show_col_nos += "    " + str(col)

    #displays the column numbers over the columns
    print(show_col_nos)
    
    #prints a top layer of underscores. 
    print("\t " + "_____" + "______" * (cols - 1))

    #loops through each row index
    for row in range(rows):

        #if row is single digit (row at index 9 is row 10), prints out the board with an extra space to line up the row numbers
        if row < 9:

            #prints out spacing times the amount of columns
            print("\t|" + stv * cols)

            #declares a variable to space out the row number
            space = "    " + str(row + 1) + "   |  "

            #loops through each column index at every row index
            for col in range(cols):

                #space variable plus the value shown to the user at each row and column
                space += (str(shown_values[row][col]) + "  |  ")

            #shows the value at every row and column
            print(space)

            #prints underscore spacing times the amount of columns
            print("\t|" + stu * cols)

        #if row is double digit, remove a space before displaying the row number to line up row numbers and the field's rows
        else:

            #prints out spacing times the amount of columns
            print("\t|" + stv * cols)

            #declares a variable to space out the row number
            space = "   " + str(row + 1) + "   |  "

            #loops through each column index at every row index
            for col in range(cols):

                #space variable plus the value shown to the user at each row and column
                space += (str(shown_values[row][col]) + "  |  ")

            #shows the value at every row and column
            print(space)

            #prints underscore spacing times the amount of columns
            print("\t|" + stu * cols)

    #on my screen, if the rows are more than 9, the columns numbers are hidden outside of view when waiting for a row and column input
    #printing the column numbers on the bottom of the field as well helps make the input process more user friendly
    if rows >= 10:

        #prints column numbers
        print("\n" + show_col_nos)

    #prints the remaining hidden mines for the user at the bottom left corner of the field
    print("\nmines left: {}".format(mines_left))



#function that sets the mines randomly in the playing field
def set_mines():

    #provides the global values needed in the function
    global rows
    global cols
    global mines_no
    global hidden_values

    #establishes a count starting at zero
    count = 0

    #while the count is less than the number of mines, continues through the loop
    while count < mines_no:

        #chooses a random integer in range 0 to the amount of rows - 1 (used as indices)
        rand_row = random.randint(0, rows - 1)

        #chooses a random integer in range 0 to the amount of columns - 1 (used as indices)
        rand_col = random.randint(0, cols - 1)

        #if the hidden value at the random row and column is not a mine and it isn't adjacent to the first row and column chosen
        if hidden_values[rand_row][rand_col] != -1 and hidden_values[rand_row][rand_col] != 9:

            #sets the hidden value at that random row and column to be a mine (the value -1 represents a mine)
            hidden_values[rand_row][rand_col] = -1

            #increments the count
            count += 1



#function that sets the value of each space in the field
def set_values():

    #provides the global values needed in the function
    global rows
    global cols
    global hidden_values
    
    #loops through each row index
    for row in range(rows):

        #loops through each column index for every row index
        for col in range(cols):

            #if the value at each cell is not a mine
            if hidden_values[row][col] != -1:

                #checks to see if adjacent cells are mines. If True, increments the hidden value of the cell +1
                #check up
                if row > 0 and hidden_values[row - 1][col] == -1:
                    hidden_values[row][col] += 1

                #check down
                if row < rows - 1 and hidden_values[row + 1][col] == -1:
                    hidden_values[row][col] += 1

                #check left
                if col > 0 and hidden_values[row][col - 1] == -1:
                    hidden_values[row][col] += 1

                #check right
                if col < cols - 1 and hidden_values[row][col + 1] == -1:
                    hidden_values[row][col] += 1

                #check upper left
                if row > 0 and col > 0 and hidden_values[row - 1][col - 1] == -1:
                    hidden_values[row][col] += 1

                #check upper right
                if row > 0 and col < cols - 1 and hidden_values[row - 1][col + 1] == -1:
                    hidden_values[row][col] += 1

                #check lower right
                if row < rows - 1 and col < cols - 1 and hidden_values[row + 1][col + 1] == -1:
                    hidden_values[row][col] += 1

                #check lower left
                if row < rows - 1 and col > 0 and hidden_values[row + 1][col - 1] == -1:
                    hidden_values[row][col] += 1



#function called when a zero valued space is chosen. This function displays all neighboring spaces until a non-zero space is reached
def neighbors(row, col, visited):

    #provides the global values needed in the function
    global rows
    global cols
    global shown_values
    global hidden_values

    #base case of recursive function. visited keeps track of cells visited, and ends the function once all zero cells and adjacent numbered cells have been revealed
    if (row, col) not in visited:

        #adds cell to visited
        visited.append((row, col))

        #if cell value equals 0, display cell and recursively run all neighboring cells back through the function
        if hidden_values[row][col] == 0:

            #Display 0 valued cell
            shown_values[row][col] = hidden_values[row][col]

            #run neighboring cells back through the function
            if row > 0:
                neighbors(row - 1, col, visited)

            if row < rows - 1:
                neighbors(row + 1, col, visited)

            if col > 0:
                neighbors(row, col - 1, visited)

            if col < cols - 1:
                neighbors(row, col + 1, visited)

            if row > 0 and col > 0:
                neighbors(row - 1, col - 1, visited)

            if row > 0 and col < cols - 1:
                neighbors(row - 1, col + 1, visited)

            if row < rows - 1 and col < cols - 1:
                neighbors(row + 1, col + 1, visited)

            if row < rows - 1 and col > 0:
                neighbors(row + 1, col - 1, visited)
                
        #if cell not equal to 0, display cell but don't run the cell back through the function        
        if hidden_values[row][col] != 0:
            shown_values[row][col] = hidden_values[row][col]
    


#function called to clear clutter in terminal
def clear_terminal():
    os.system("clear")



#function called to give the user intructions of how to input their selections
def instructions():
    print("\nInstructions:")
    print("1. To select a cell, enter a row and column number, and press Enter. (example: '23' selects the cell at row 2 and column 3.)")
    print("2. To flag a cell, enter a row and column number followed by 'f'. (example: '23f')")
    print("3. If you want to unflag a cell, simply enter the row and column number followed by 'f' again.")
    print("4. Enter 'q' to exit the game at any time.")


#function that receives user input and returns a row and column and whether to select or flag it
def user_input():

    #provides the global values needed in the function
    global shown_values
    global rows
    global cols

    #gathers the row and column and operation from the user
    inp = input("\nPlease enter a cell to select or flag... ")

    #if user enters h, shows the instructions again and restarts the function
    if inp.lower() == "h":
        instructions()
        return user_input()

    #if user opts to quit the game
    if inp.lower() == "q":

       #provides a cancel option if the user accidentally entered q
        qut = input("\n\nAre you sure you want to quit? (y/n)... ")

        #upper or lower case 'y' will confirm quit
        if qut.lower() == "y":

            #prints goodbye and exits the game
            print("\nGoodbye!")
            quit()

        #if user backs out of quitting, the function is restarted
        else:
            return user_input()

    #if user enters 2 characters
    if len(inp) == 2:

        #makes sure both characters entered can be converted to integers and simultaneously sets the row and column indices
        try:
            row = int(inp[0]) - 1
            col = int(inp[1]) - 1
        
        #if either of the entered characters can't be converted to integers
        except:

            #prints error message and restarts function
            print("\nInput error! If you need help, enter 'h' to see instructions")
            return user_input()

        #returns row and column as a tuple
        return (row, col)

    #if user enters 3 characters
    elif len(inp) == 3:

        #if the 3rd character entered is f or F
        if inp[2].upper() == "F":

            #makes sure the 1st and 2nd characters can be converted to integers and simultaneously sets the row and column indices
            try:
                row = int(inp[0]) - 1
                col = int(inp[1]) - 1

            #if either the 1st or 2nd character can't be converted to integers
            except:

                #prints error message and restarts function
                print("\nInput error! If you need help, enter 'h' to see instructions")
                return user_input()

            #returns row, column, and flag indication as a tuple
            return (row, col, "F")

        #if 3rd character isn't f or F
        else:

            #makes sure all characters can be converted to integers and sets each character to an accessible variable
            try:
                int_1 = int(inp[0]) - 1
                int_2 = int(inp[1]) - 1
                int_3 = int(inp[2]) - 1

            #if any of the entered characters can't be converted to integers
            except:

                #prints error message and restarts function
                print("\nInput error! If you need help, enter 'h' to see instructions")
                return user_input()

            #a few if then statements are needed to dissect the input.
            #the input could mean a couple things to the game. For instance, input '111' could be interpreted as row '11, col '1'
            #or row '1', col '11'. the solution to this instance is provided in the following if then statements

            #if the 1st 2 integers are greater than the amount of rows and the last 2 integers are less than or equal to the amount of columns
            #or if the 3rd integer is a zero
            if int(inp[:2]) > rows and int(inp[1:]) <= cols or int(inp[2]) == 0:

                #sets the row to the 1st integer and the column to the 2nd and 3rd integers
                row = int_1
                col = int(inp[1:]) - 1

                #returns row and column as a tuple
                return (row, col)

            #else if the 1st 2 integers are less than or equal to the amount of rows and the last 2 integers are greater than the amount of columns
            #or if the 2nd integer is zero
            elif int(inp[:2]) <= rows and int(inp[1:]) > cols or int(inp[1]) == 0:

                #then sets row to 1st 2 integers and column to the 3rd integer
                row = int(inp[:2]) - 1
                col = int_3

                #returns row and column as a tuple
                return (row, col)

            #otherwise the digits can be interpreted both ways
            else:

                #checks to see if one of the interpretations has already been revealed
                #(example: if row 1, col 11 has already been revealed, then it's assumed the user meant row 11, col 1)
                if type(shown_values[int_1][int(inp[1:]) - 1]) == int:
                    
                    #sets row to the 1st and 2nd integers and column to the 3rd integer
                    row = int(inp[:2]) - 1
                    col = int_3

                    #returns row and column as a tuple
                    return (row, col)

                #checks to see if the other interpretation has already been revealed
                #(example: if row 11, col 1 has already been revealed, then it's assumed the user meant row 1, col 11)
                elif type(shown_values[int(inp[:2]) - 1][int_3]) == int:

                    #sets row to 1st integer and column to the 2nd and 3rd integers
                    row = int_1
                    col = int(inp[1:]) - 1

                    #returns row and column as a tuple
                    return (row, col)

                #if both interpretations are available to be selected
                else:

                    #prints a message to the user of the situation
                    print("\nInput entered can mean 1 of 2 available cells.")

                    #asks the user to clarify 
                    clarify = input("\nIf you want to select row: {}, col: {},  enter '1'.  If you want to select row: {}, col: {},  enter '2'... ".format(int_1 + 1, int(inp[1:]), int(inp[:2]), int_3 + 1))
                    
                    #if user chooses the first option
                    if clarify == "1":

                        #sets row to the 1st integer and column to the 2nd and 3rd integers
                        row = int_1
                        col = int(inp[1:]) - 1

                        #returns row and column as a tuple
                        return (row, col)

                    #if user chooses the 2nd option
                    elif clarify == "2":

                        #sets row to the 1st and 2nd integers and column to the 3rd integer
                        row = int(inp[:2]) - 1
                        col = int_3

                        #returns row and column as a tuple
                        return (row, col)
                    
                    #any other input triggers an error message and restarts the function
                    else:
                        print("\nInput error! If you need help, enter 'h' to see instructions")
                        return user_input()

    #else if the user inputs 4 characters    
    elif len(inp) == 4:

        #if the last character is 'f' or 'F'
        if inp[3].upper() == "F":
            
            #makes sure the 1st 3 characters are integers and sets them to an accessible variable
            try:
                int_1 = int(inp[0]) - 1
                int_2 = int(inp[1]) - 1
                int_3 = int(inp[2]) - 1

            #if any of the entered characters can't be converted to integers
            except:

                #prints error message and restarts the function
                print("\nInput error! If you need help, enter 'h' to see instructions")
                return user_input()

            #if the 1st 2 integers are greater than the amount of rows and the 2nd and 3rd integers are less than or equal to the amount of columns
            #or if the 3rd integer is a zero
            if int(inp[:2]) > rows and int(inp[1:3]) <= cols or int(inp[2]) == 0:

                #sets row to 1st integer and column to 2nd and 3rd integers
                row = int_1
                col = int(inp[1:3]) - 1

                #returns row, column, and flag indication as a tuple
                return (row, col, "F")

            #else if the 1st 2 integers are less than or equal to the amount of rows and the 2nd and 3rd integers are greater than the amount of columns
            #or if the 2nd integer is zero
            elif int(inp[:2]) <= rows and int(inp[1:3]) > cols or int(inp[1]) == 0:

                #sets the row to the 1st and 2nd integer and sets col to the 3rd integer
                row = int(inp[:2]) - 1
                col = int_3

                #returns row, column, and flag indication as a tuple
                return (row, col, "F")

            #otherwise the digits can be interpreted both ways
            else:

                #checks to see if one of the interpretations has already been revealed
                #(example: if row 1, col 11 has already been revealed, then it's assumed the user meant row 11, col 1)
                if type(shown_values[int_1][int(inp[1:3]) - 1]) == int:
                    
                    #sets row to the 1st and 2nd integers and sets column to the 3rd integer
                    row = int(inp[:2]) - 1
                    col = int_3

                    #returns row, column, and flag indication as a tuple
                    return (row, col, "F")

                #checks to see if the other interpretation has already been revealed
                #(example: if row 11, col 1 has already been revealed, then it's assumed the user meant row 1, col 11)
                elif type(shown_values[int(inp[:2]) - 1][int_3]) == int:

                    #sets the row to the first integer and sets the column to the 2nd and 3rd integers
                    row = int_1
                    col = int(inp[1:3]) - 1

                    #returns row, column, and flag indication as a tuple
                    return (row, col, "F")

                #if both interpretations are able to be selected
                else:

                    #prints a message to the user of the situation
                    print("\nInput entered can mean 1 of 2 available cells.")

                    #asks the user to clarify
                    clarify = input("\nIf you want to select row: {}, col: {},  enter '1'.  If you want to select row: {}, col: {},  enter '2'... ".format(int_1 + 1, int(inp[1:3]), int(inp[:2]), int_3 + 1))
                    
                    #if user chooses option 1
                    if clarify == "1":

                        #sets the row to the 1st integer and sets the column to the 2nd and 3rd integers
                        row = int_1
                        col = int(inp[1:3]) - 1

                        #returns row, column, and flag indication as a tuple
                        return (row, col, "F")

                    #if user chooses option 2
                    elif clarify == "2":

                        #sets the row to the 1st and 2nd integers and sets the column to the 3rd integer
                        row = int(inp[:2]) - 1
                        col = int_3

                        #returns row, column, and flag indication as a tuple
                        return (row, col, "F")
                    
                    #any other input triggers an error message and restarts the function
                    else:
                        print("\nInput error! If you need help, enter 'h' to see instructions")
                        return user_input()

        #if the last character is not an 'f' or 'F'
        else: 

            #makes sure all characters entered can be converted to integers and stores them to an accessible variable
            try:
                int_1 = int(inp[0]) - 1
                int_2 = int(inp[1]) - 1
                int_3 = int(inp[2]) - 1
                int_4 = int(inp[3]) - 1

            #if any character can't be converted to an integer
            except:

                #prints error message and restarts the function
                print("\nInput error! If you need help, enter 'h' to see instructions")
                return user_input()

            #sets the row to the 1st and 2nd integers and sets the column to the 3rd and 4th integers
            row = int(inp[:2]) - 1
            col = int(inp[2:]) - 1

            #returns the row and column as a tuple
            return (row, col)
    
    #if the length of the input is 5 and if the last character is 'f' or 'F'
    elif len(inp) == 5 and inp[4].upper() == "F":

        #makes sure the 1st 4 characters can be converted to integers and stores them to accessible variables
        try:
            int_1 = int(inp[0]) - 1
            int_2 = int(inp[1]) - 1
            int_3 = int(inp[2]) - 1
            int_4 = int(inp[3]) - 1

        #if either of the 1st 4 characters can't be converted to integers
        except:

            #prints error message and restarts the function
            print("\nInput error! If you need help, enter 'h' to see instructions")
            return user_input()

        #sets the row to the 1st and 2nd integers and sets the column to the 3rd and 4th integers
        row = int(inp[:2]) - 1
        col = int(inp[2:4]) - 1

        #returns row, column, and flag indication as a tuple
        return (row, col, "F")
        
    #any other input will trigger an error message and restart the function
    else:
        print("\nInput error! If you need help, enter 'h' to see instructions")
        return user_input()


#function called to check if the game is over
def game_over():

    #provides the global values needed in the function
    global rows
    global cols
    global shown_values
    global hidden_values
    global mines_no
    global flags

    #initializes the variable count at zero
    count = 0 

    #loops through each row index
    for row in range(rows):

        #loops through each column index at each row index
        for col in range(cols):

            #if the shown value at each cell is not blank and is not flagged
            if shown_values[row][col] != " " and shown_values[row][col] != "\033[1;33;40mF\033[0m":

                #increment the count
                count += 1

    #if count equal the total amount of cells minus the number of mines
    if count == rows * cols - mines_no:
        return True

    else: 
        return False



#function called to show the mines in the playing field 
def show_mines(win):

    #provides the global values needed in the function
    global rows
    global cols
    global hidden_values
    global shown_values

    #loops through each row index
    for row in range(rows):

        #loops through each column index for each row index
        for col in range(cols):

            #if win equals True
            if win:

                #if the cell is a mine
                if hidden_values[row][col] == -1:

                    #sets the cell to an M
                    #"\033[1;32;40mM\033[0m" shows the M in green with a black background that highlights the mine locations better
                    shown_values[row][col] = "\033[1;32;40mM\033[0m"
            
            #if win equals False
            else:

                #if the cell is a mine
                if hidden_values[row][col] == -1:

                    #sets the cell to an M
                    #"\033[1;40mM\033[0m" shows the M with a black background that highlights the mine locations better
                    shown_values[row][col] = "\033[1;40mM\033[0m"


#establishes play_game as True
play_game = True

#establishes win as True
win = True

#while play_game equals True
while play_game:

    #clears terminal at the beginning of each loop
    clear_terminal()

    #prints greeting message
    print("\n\n\nWelcome to my humble game of Minesweeper.")

    #calls function to ask user for field size
    rows_cols = field_size()

    #estabilishes the amount of rows and columns for the game
    rows = rows_cols[0]
    cols = rows_cols[1]
    total_cells = rows * cols

    #every shown value starts as a blank space
    shown_values = [[" " for c in range(cols)] for r in range(rows)]

    #every hidden value begins at zero
    hidden_values = [[0 for c in range(cols)] for r in range(rows)]

    #prints explanatory message
    print("\n\nDifficulty is determined by the ratio of mines to cells in the field. (easy = 15% mines, med = 20% mines, and hard = 25% mines)")
    
    #asks user for the difficulty and establishes the number of mines used in the game. It also changes the value from a float to an integer(no decimals)
    mines_no = int(difficulty() * total_cells)

    #establishes the amount of flags used at zero
    flags = 0

    #establishes that the user hasn't reached their limit of flags to use
    too_many_flags = False

    #displays the field to the user
    print_field(mines_no)

    #displays the game play instructions
    instructions()

    #Lets the user know how many mines are hidden
    print("\nThere are {} mines hidden in the field. Good luck!".format(mines_no))
    
    #establishes that this is the first time through the loop
    first = True

    #while it is the first time through the loop
    while first:

        #prompts the user to select a cell
        cell_inp = user_input()

        #sets row to the first object of the returned tuple
        row = cell_inp[0]

        #sets column to the 2nd object of the returned tuple
        col = cell_inp[1]

        #if row index is greater than the amount of available rows or row index is less than 0
        #or column index is greater than the amount of columns or column index is less than 0
        if row + 1 > rows or row < 0 or col + 1 > cols or col < 0:

            #prints error message, runs back through the loop
            print("\nInput Error: Enter an available cell")
            continue

        #the following statements set the chosen cell and its adjacent cells apart from the other values in order that a mine cannot be set in these cells
        #this order of operation ensures that the first cell selected will always be a zero valued cell and the mines will be placed randomly about these cells
        
        #set the selected cell apart
        hidden_values[row][col] = 9

        #if the selected row is not the first row, set the cell above apart
        if row > 0:
            hidden_values[row - 1][col] = 9
        
        #if the selected row is not the last row, set the cell below apart
        if row < rows - 1:
            hidden_values[row + 1][col] = 9
        
        #if the selected column is not the first column, set the cell to the left apart
        if col > 0:
            hidden_values[row][col - 1] = 9
            
        #if the selected column is not the last column, set the cell to the right apart
        if col < cols - 1:
            hidden_values[row][col + 1] = 9
        
        #if the selected row is not the first row and the selected column is not the first column, set the cell to the upper left apart
        if row > 0 and col > 0:
            hidden_values[row - 1][col - 1] = 9
            
        #if the selected row is not the first row and the selected column is not the last column, set the cell to the upper right apart
        if row > 0 and col < cols - 1:
            hidden_values[row - 1][col + 1] = 9
        
        #if the selected row is not the last row and the selected column is not the last column, set the cell to the lower right apart
        if row < rows - 1 and col < cols - 1:
            hidden_values[row + 1][col + 1] = 9
            
        #if the selected row is not the last row and the selected column is not the first column, set the cell to the lower left apart
        if row < rows - 1 and col > 0:
            hidden_values[row + 1][col - 1] = 9
            
        #set the mines randomly in the playing field around the cells that have been set apart
        set_mines()

        #after setting the mines, set all the cells that were set apart back to zero
        hidden_values[row][col] = 0

        if row > 0:
            hidden_values[row - 1][col] = 0
        
        if row < rows - 1:
            hidden_values[row + 1][col] = 0
            
        if col > 0:
            hidden_values[row][col - 1] = 0
            
        if col < cols - 1:
            hidden_values[row][col + 1] = 0
            
        if row > 0 and col > 0:
            hidden_values[row - 1][col - 1] = 0
            
        if row > 0 and col < cols - 1:
            hidden_values[row - 1][col + 1] = 0
            
        if row < rows - 1 and col < cols - 1:
            hidden_values[row + 1][col + 1] = 0
            
        if row < rows - 1 and col > 0:
            hidden_values[row + 1][col - 1] = 0

        #set the number values of all the cells that are adjacent to mines
        set_values()

        #if the user selects a cell to reveal
        if len(cell_inp) == 2:

            #flips first to false to enter the game loop
            first = False

            #displays the hidden value of the selected cell
            shown_values[row][col] = hidden_values[row][col]

            #establishes visited as an empty list for the neighbors function
            visited = []

            #knowing that the first cell selected is zero, runs the neighbors function to display all the adjacent cells until reaching a non-zero cell
            neighbors(row, col, visited)

        #if the user flags a cell
        if len(cell_inp) == 3:

            #if the shown value at that cell is a blank space
            if shown_values[row][col] == " ":

                #replaces the blank space with a yellow F with a black background
                shown_values[row][col] = "\033[1;33;40mF\033[0m"

                #increments flags used
                flags += 1

            #if the shown value at that cell is already flagged
            elif shown_values[row][col] == "\033[1;33;40mF\033[0m":

                #replaces the F with a blank space
                shown_values[row][col] = " "

                #decrements flags used
                flags -= 1
        
            #otherwise run back through the loop
            else:
                continue


    #loops through the game function until game_over() == True
    while not game_over():

        #clears_terminal at beginning of each loop
        clear_terminal()

        #mines left is equal to the number of mines minus the flags used
        mines_left = mines_no - flags

        #displays the field to the user
        print_field(mines_left)

        #if the user tries to use more flags than there are mines, print instructional message
        if too_many_flags:
            print("\nYou entered more flags than there are hidden mines. Try again.")
        
        #asks user to select a cell
        cell_inp = user_input()

        #sets row to first object in returned tuple
        row = cell_inp[0]

        # sets column to 2nd object in returned tuple
        col = cell_inp[1]

        #if row index is greater than the amount of available rows or row index is less than 0
        #or column index is greater than the amount of columns or column index is less than 0
        if row + 1 > rows or row < 0 or col + 1 > cols or col < 0:

            #prints error message and runs back through the loop
            print("\nInput Error: Enter an available cell")
            continue

        # if the user selects a cell to reveal
        if len(cell_inp) == 2:

            # if the selected cell is a mine
            if hidden_values[row][col] == -1:

                # flip win to False
                win = False

                # changes all values that are -1 to M
                show_mines(win)

                # displays the hit mine in red
                shown_values[row][col] = "\033[1;31;40mM\033[0m"

                # displays the mine ridden field to the user
                print_field(0)

                #prints Game over message
                print("\n\nYou hit a mine and blew up! Game Over... ")

                # breaks game loop
                break

            # if the selected cell is 0
            elif hidden_values[row][col] == 0:

                # establishes visited as an empty list for the neighbors function
                visited = []

                # calls neighbors to display adjacent cells until reaching a non-zero cell
                neighbors(row, col, visited)

            # otherwise the cell is a non-zero number which is displayed to the user
            else:
                shown_values[row][col] = hidden_values[row][col]

        # if the user flags a cell
        if len(cell_inp) == 3:

            # if the amount of flags used is less than the number of mines
            if flags < mines_no:

                # if the shown value at the cell is a blank space
                if shown_values[row][col] == " ":

                    # replaces blank space with yellow F
                    shown_values[row][col] = "\033[1;33;40mF\033[0m"

                    # increments flags used
                    flags += 1

                # if the shown value at the cell is flagged
                elif shown_values[row][col] == "\033[1;33;40mF\033[0m":

                    # replaces F with blank space
                    shown_values[row][col] = " "

                    # decrements flags used
                    flags -= 1

                # otherwise run back through the loop
                else:
                    continue
            
            # if the amount of flags used is greater than or equal to the number of mines
            else:
    
                # if the shown value at the cell is a blank space
                if shown_values[row][col] == " ":

                    # flip too_many_flags to True
                    too_many_flags = True

                # if the cell is flagged
                elif shown_values[row][col] == "\033[1;33;40mF\033[0m":

                    # replaces the F with a blank space
                    shown_values[row][col] = " "

                    # decrements the flags used
                    flags -= 1
                
                # otherwise run back through the loop
                else:
                    continue

    
    # if win equals True
    if win:

        # updates the cells that equal -1 to a green M and print the field with a congratulatory message
        show_mines(win)
        print_field(0)
        print("\n\nCongratulations!! You made it through the field without dying!!")
        
    # asks the user if they would like to play again
    play_again = input("\n\nWould you like to play again? (y/n)... ")

    # if the user chooses yes
    if play_again.lower() == "y":

        # play_game remains True and the game will run again
        play_game = True

    # otherwise play_game flips to False and the game loop is ended and that concludes the program
    else:
        play_game = False
