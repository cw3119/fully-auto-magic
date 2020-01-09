#Tic-Tac-Toe Two Revengance Featuring Dante from Devil may cry, & Knuckles
def winningBoard(list1):
    winner = False
    #Checks rows for a horizontal victor
    count= 0
    for x in list1:
        
        if list1[count][0] == list1[count][1] == list1[0][2] and list1[count][0] !='':
            winner= list1[count][0]
        count+=1
    #Checks rows for a vertical victor
    count= 0
    for y in list1:
        if list1[0][count] == list1[1][count] == list1[2][count] and list1[0][count] !='':
            winner= list1[0][count]
        count+=1
    #Checks rows for a diagonal victor
        
    for y in list1:
        if list1[0][0] == list1[1][1] == list1[2][2] and list1[0][0] !='':
            winner= list1[0][0]
        elif list1[0][2] == list1[1][1] == list1[2][0] and list1[0][2] !='':
            winner= list1[0][2]
    return(winner)

def isDraw(board):
    for row in board:
        for col in row:
            if col !='X' and col !='O':
                return(False)
    return(True)

board = [ ['1','2','3'],['4','5','6'],['7','8','9']]
victor=False
totalTurns=1

while victor==False:
    if isDraw(board)==True:
        break
    if totalTurns%2==1:
        turn="X"
    else:
        turn="O"
    #beginning of turn
    for line in board:
        print(line)
    pMove= input(turn + " where would you like to play? ")
    #Ensures the move has been placed. For instance if user enters 2, then decideds to move to 1 this value will allow it
    placed=False
    while not placed :
        #1
        if pMove == board[0][0]:
            board[0][0]=turn
            placed=True
        #2    
        elif pMove == board[0][1] and placed == False:
            board[0][1]=turn
            placed=True 
        #3
        elif pMove == board[0][2] and placed == False:
            board[0][2]=turn
            placed=True
        #4
        elif pMove == board[1][0] and placed == False:
            board[1][0]=turn
            placed=True
        #5

        elif pMove == board[1][1] and placed == False:
            board[1][1]=turn
            placed=True
        #6
        elif pMove == board[1][2] and placed == False:
            board[1][2]=turn
            placed=True
        #7
        elif pMove == board[2][0] and placed == False:
            board[2][0]=turn
            placed=True
        #8
        elif pMove == board[2][1] and placed == False:
            board[2][1]=turn
            placed=True
        #9
        elif pMove == board[2][2] and placed == False:
            board[2][2]=turn
            placed=True
        else:
            print("Oh that spot is taken, Try again")
            pMove= input(turn+" where would you like to play? ")
        
    totalTurns= totalTurns+1       
    victor=winningBoard(board)
    
if winningBoard(board) =='X' or winningBoard(board)=='O':
    print("We have a winner! Congratulations "+winningBoard(board)+"!!!")
else:
    print("Draw!")
    
for line in board:
    print(line)
