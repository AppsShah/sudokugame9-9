
board=[
[2,3,0,4,1,5,0,6,8], 
[0,8,0,2,3,6,5,1,9],
[1,6,0,9,8,7,2,3,4], 
[3,1,7,0,9,4,0,2,5],
[4,5,8,1,2,0,6,9,7],
[9,2,6,0,5,8,3,0,1],
[0,0,0,5,0,0,1,0,2],
[0,0,0,8,4,2,9,0,3],
[5,9,2,3,7,1,4,8,6] ]
def print_board(board):
    for row in range(0,9):
        for col in range(0,9):
            print(board[row][col],end=" ")
        print("")
def rulecheck(board,row,col,num):
    # rows ka liya 
    for i in range(0,9):
        if(board[row][i]==num):
            return False
    return True
    # col ka liya
    for j in range(0,9):
        if(board[i][col]==num):
            return False
    return True
    # square ka liya 
    rowbox= row - row%3
    colbox= col - col%3
    for i in range(rowbox,rowbox+3):
        for j in range(colbox,colbox+3):
            if board[i][j]==num:
                return False
    return True
    
def sudokusolver(board):
    row=-1
    col=-1
    isempty=False
    for i in range(0,9):
        for j in range(0,9):
            if board[i][j]==0:
                isempty=True
                row=i
                col=j
                break
        if isempty==True:
            break
    if isempty==False:
        return True
    for num in range(1,10):
        if(rulecheck(board,row,col,num)==True):
            board[row][col]=num
            if(sudokusolver(board)==True):
                return True
            board[row][col]==0
    return False
#sudokusolver(board)
#board2print()
print("----------------------------------------")
#print_board(board)

