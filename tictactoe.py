board = ["-","-","-",
         "-","-","-",
         "-","-","-"]

gameRunning = True
currentPlayer = "X"
winner = None

def changePlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"
    
def printboard():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("----------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("----------")
    print(board[6] + " | " + board[7] + " | " + board[8])

def selection():
    try:
        choice = int(input("Pick a square 1-9: "))
        if board[choice-1] == "-":
            board[choice-1] = currentPlayer
        else:
            print("This square has already been selected.")
    except ValueError:
        print("You didn't enter a valid number.")

def CheckIfWin():
    global gameRunning
    if checkHorizontal():
        printboard()
        print(f"{winner} Wins!")
        gameRunning=False
        
    elif checkVertical():
        printboard()
        print(f"{winner} Wins!")
        gameRunning=False
        
    elif checkDiagonal():
        printboard()
        print(f"{winner} Wins!")
        gameRunning=False
    
def checkIfTie():
    global gameRunning
    if "-" not in board and winner==None:
        gameRunning=False
        printboard()
        print("Its a tie!")

def checkHorizontal():
    global winner
    if board[0]==board[1]==board[2] and board[0] != "-":
        winner = board[0]
        return True
    elif board[3]==board[4]==board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board [8] and board[6] != "-":
        winner = board[6]
        return True

def checkVertical():
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True

def checkDiagonal():
    global winner
    if board[0]==board[4]==board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2]==board[4]==board[6] and board[2] != "-":
        winner = board[2]
        return True

while gameRunning:
    printboard()
    selection()
    CheckIfWin()
    checkIfTie()
    changePlayer()
