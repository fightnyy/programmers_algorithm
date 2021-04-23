def check_row(board, i, j):
    cnt = 0
    for w in range(1,len(board)-j):
        if board[i][w+j] == 1:
            cnt+=1
        else :
            break
    return cnt
def check_col(board, n_row, i, j):
    for  in range(board):
def solution(board):
    result = -1
    for i in range(len(board)):
        cnt = 0
        for j in range(len(board)):
            if board[i][j] == 1:
                n_row=check_row(board,i,j) #가로 확인
                n_col=check_col(board,n_row,i,j)