def print_board(board):
    for x in board:
        print ' '.join(x)
        
def game_begins():  
    board = [] 
    print "Please enter the size of the board",
    size = input()
    for x in range(size):
        board.append(["-"] * size)
    print_board(board)
    if (size == 1):
        return "You can't play tic-tac-toe"
    for i in range(size*size):
        if (i%2==0):
            print "Player 1"
        else:
            print "Player 2"
        print "Enter row and column", 
        a,b = map(int,raw_input().split())
        
        if ( a > 0 and a <= size and b > 0 and b <= size):
            if (board[a-1][b-1] == "X" or board[a-1][b-1] == "O"):
                print "You already entered"
            else:
                if (i%2==0):
                    board[a-1][b-1] = 'X'
                else:
                    board[a-1][b-1] = 'O'
            print_board(board)
        else:
            print "Out of board"
        
        if i in range(size**2-1):
            for i in range(size):
                a, b = 0, 0
                for j in range(size):
                    if (board[j][i] == "X"):
                        a +=1
                        if (a == size):
                            return "Player 1 wins! Game Over"
                    elif (board[j][i] == "O"):
                        b +=1
                        if (b == size):
                            return "Player 2 wins! Game Over"
            for j in range(size):
                c, d = 0, 0
                for i in range(size):
                    if (board[j][i] == "X"):
                        c +=1
                        if (c == size):
                            return "Player 1 wins! Game Over"
                    elif (board[j][i] == "O"):
                        d +=1
                        if (d == size):
                            return "Player 2 wins! Game Over"
            e, f = 0, 0
            for k in range(size):
                if (board[k][k] == "X"):
                    e += 1
                    if (e == size):
                        return "Player 1 wins! Game Over"
                elif (board[k][k] == "O"):
                    f += 1
                    if (f == size):
                        return "Player 2 wins! Game Over"
            
        elif (i == (size*size)-1):
            return "Draw match! Game Over"
    
def rep():
    c = raw_input()
    if (c == 'y'):
        print game_begins()
        print "Do you want to play again? y/n"
        rep()
        
    elif (c == 'n'):
        print "Have a nice day"
    else:
        print "invalid input"
        game()  
        
def game():    
    print "Do you want to play tic-tac-toe? y/n"
    rep()
    
game()