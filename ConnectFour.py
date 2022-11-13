import random


#Sets up lists with six entries that will represent each column
columnOne = [" "]*6
columnTwo = [" "]*6
columnThree = [" "]*6
columnFour = [" "]*6
columnFive = [" "]*6
columnSix = [" "]*6
columnSeven = [" "]*6
columns = [columnOne,columnTwo,columnThree,columnFour,columnFive,columnSix,columnSeven] #A master list, which is composed of each column, so that they are easily accessible

integers = [0,1,2,3,4,5] #Lists with specific numbers which will be used later on
rows = [0,1,2,3,4,5]


def makeMove(letter,choice): #The function used to make player moves
    for i in integers:
        if columns[choice][i] == " ": #It will go through each entry in the column of choice, starting with the bottom, until it finds an empty space, which is then filled with the respective players letter
            columns[choice][i] = letter
            break

def drawBoard(): #Prints the game board
    print("  1   2   3   4   5   6   7 ") #Column indicators
    row = 5
    while row >= 0: #row begins at 5 so that the bottom row is the zero row, meaning each column list starts at the bottom of the board
        print("+---"*7,"+",sep="")
        print("|   "*7,"|",sep="")
        print("| "+columnOne[row]+" | "+columnTwo[row]+" | "+columnThree[row]+" | "+columnFour[row]+" | "+columnFive[row]+" | "+columnSix[row]+" | "+columnSeven[row]+" | " )
        print("|   "*7,"|",sep="")
        row -= 1
    print("+---"*7,"+",sep="")

def win(letter): #Checks if the player won
    for i in columns: #Checks if they've won with four in a row in a column
        j=0
        while j<=2: #used while rather than for b/c it allows for more flexibility in this case, cause I only want it to run for the first three
            if i[j]==letter and letter==i[j+1] and letter==i[j+2] and letter==i[j+3]: #if four entries in a row are the same letter, this player has won
                return True
            else:
                j+=1 #Previously the program starts counting from the bottom, by adding one it will count again starting from the second row

    for i in rows: #Checks if they've won with four in a row in a row. Rows is an integer list that was previously defined
        j=0 #Start at the first column
        while j<=4: #After you reach a certain point, four in a row is not possible. This while loop will stop running at that point
            if columns[j][i]==letter and columns[j+1][i]==letter and columns[j+2][i]==letter and columns[j+3][i]==letter:
                return True
            else:
                j+=1
    k=0
    while k<=3: #checks for a diagonal win, left to right (left being the bottom)
        for i in [0,1,2]:
            if columns[k][i] == letter and columns[k+1][i+1]==letter and columns[k+2][i+2]==letter and columns[k+3][i+3]==letter:
                return True
        k+=1
    k=6
    while k>=3: #checks for a diagonal win, right to left (right being the bottom)
        for i in [0,1,2]:
            if columns[k][i] == letter and columns[k-1][i+1]==letter and columns[k-2][i+2]==letter and columns[k-3][i+3]==letter:
                return True
        k-=1

letterChoice = input("Will player one be X or O: ") #This is the beginning of the actual game

while True: #Properly assigns each player their respective letter
    if letterChoice.upper().startswith("X"):
        playerLetter = "X"
        player2Letter = "O"
        break
    elif letterChoice.upper().startswith("O"):
        playerLetter = "O"
        player2Letter = "X"
        break
    else:
        letterChoice = input("Will you be X or O?")

turn = "player"

drawBoard()

while True: #The code for the game is contained within this while loop
    if turn == "player":
        choice = int(input("Please enter the column player one wishes to play in: "))
        if choice > 7 or choice < 1: #If they haven't entered a valid column, they will be reprompted
            print("enter a valid column")
            continue
        if columns[choice-1][5] != " ":
            continue
        makeMove(playerLetter,choice-1) #choice-1 is done because lists start at 0, rather than 1
        if win(playerLetter): #checks if player one won
            drawBoard()
            print("player one won!")
            break #stops the game
        drawBoard()
        turn = "player2"
    elif turn == "player2":
        choice = int(input("Please enter the column player two wishes to play in: "))
        #choice = random.randint(0,6)
        if choice > 7 or choice < 1:
            print("enter a valid column")
            continue
        if columns[choice-1][5] != " ":
            continue
        makeMove(player2Letter,choice-1)
        if win(player2Letter):
            drawBoard()
            print("player two won!")
            break
        turn = "player"
        drawBoard()
