
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
board1 = [ ['O', '', 'X'], ['', 'O', ''], ['X', '', 'X'] ]
print("Board1:", winningBoard(board1))

board2 = [ ['X', 'X', 'X'], ['', 'O', ''], ['X', '', 'X'] ]
print("Board2:", winningBoard(board2))

 
board3 = [ ['X', 'O', 'X'], ['', 'O', ''], ['X', 'O', 'X'] ]
print("Board3:", winningBoard(board3))

board4 = [ ['X', 'O', 'X'], ['', 'X', ''], ['X', 'O', 'X'] ]
print("Board4:", winningBoard(board4))

