"""
Tic Tac Toe Player
"""

import math, copy, random

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

def player(board):
    """
    Returns player who has the next turn on a board.
    """
    # print("Players turn function")
    xcount = 0
    ocount = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                xcount += 1
            if board[i][j] == O:
                ocount += 1
    if xcount > ocount:
        # print("O's Turn Next")
        return O
    else:
        # print("X's Turn Next")
        return X

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    moves = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                moves.add((i,j))
    
    # Any return value is acceptable if a terminal board is provided as input
    if terminal(board) == True:
        return None
    return moves

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action == None:
        raise ValueError("No more actions")

    board_copy = copy.deepcopy(board)
    for i in range(3):
        for j in range(3):
            if i == action[0] and j == action[1]:
                board_copy[i][j] = player(board)
    return board_copy

def moves_left(board):
    """
    Returns True if there are any moves left to play, else returns False.
    """
    for i in range(3):
        # print(i)
        for j in range(3):
            # print(j)
            if (board[i][j] == EMPTY):
                return True
    return False

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    
    if board[0][0] == X and board[0][1] == X and board[0][2] == X:
        # print(" X won *******")
        return X
    elif board[1][0] == X and board[1][1] == X and board[1][2] == X:
        # print(" X won *******")
        return X
    elif board[2][0] == X and board[2][1] == X and board[2][2] == X:
        # print(" X won *******")
        return X
    # O across
    elif board[0][0] == O and board[0][1] == O and board[0][2] == O:
        # print(" O won *******")
        return O
    elif board[1][0] == O and board[1][1] == O and board[1][2] == O:
        # print(" O won *******")
        return O
    elif board[2][0] == O and board[2][1] == O and board[2][2] == O:
        # print(" O won *******")
        return O
    # X diagonal
    elif board[0][0] == X and board[1][1] == X and board[2][2] == X:
        # print(" X won *******")
        return X  
    elif board[0][2] == X and board[1][1] == X and board[2][0] == X:
        # print(" X won *******")
        return X      
    # O diagonal
    elif board[0][0] == O and board[1][1] == O and board[2][2] == O:
        # print(" O won *******")
        return O 
    elif board[0][2] == O and board[1][1] == O and board[2][0] == O:
        # print(" O won *******")
        return O
    # X column
    elif board[0][0] == X and board[1][0] == X and board[2][0] == X:
        # print(" X won *******")
        return X
    elif board[0][1] == X and board[1][1] == X and board[2][1] == X:
        # print(" X won *******")
        return X
    elif board[0][2] == X and board[1][2] == X and board[2][2] == X: 
        # print(" X won *******")
        return X
    # O column
    elif board[0][0] == O and board[1][0] == O and board[2][0] == O:
        # print(" O won *******")
        return O
    elif board[0][1] == O and board[1][1] == O and board[2][1] == O:
        # print(" O won *******")
        return O
    elif board[0][2] == O and board[1][2] == O and board[2][2] == O:    
        # print(" O won *******")
        return O
    # No winner
    elif moves_left(board) == False:
        # print("########## Game TIED ###########")
        return None
    else: 
        # print("No Winner *****")
        return None
    # raise NotImplementedError

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # print("terminal function")
    if winner(board) == None:
        # print("Game NOT over")
        return False
    elif winner(board) == X or winner(board) == O or moves_left(board) == False:
        # print("Terminal Board.")
        # print(len(board))
        return True
    # raise NotImplementedError

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    # print("Utility function")
    if winner(board) == X:
        # print("X won.")
        return 1
    elif winner(board) == O: 
        # print("O won.")
        return -1
    elif winner(board) == None:
        # print("Tied...")
        return 0
    # else: 
    #     # print("No winner.")
    #     return 0
    # raise NotImplementedError

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    x_moves = []
    x_count = []
    o_moves = []
    o_count = []

    def maxvalue(s):
        v = float("-inf")
        if terminal(s):
            return utility(s)
        for count_x,a in enumerate(actions(s)):
            x_count.append(count_x)
            print("X moves: ", x_count)
            print("move ",a,"\n")
            print(result(s,a))
            print("\n")
            v = max(v,minvalue(result(s,a)))
            if a not in x_moves:          
                x_moves.append(a)
        return v
    
    def minvalue(s):
        v = float("inf")
        if terminal(s):
            return utility(s)
        for count_o, a in enumerate(actions(s)):
            o_count.append(count_o)
            print("O moves: ",o_count)
            print("move ",a,"\n")
            print(result(s,a))
            print("\n")
            v = min(v,maxvalue(result(s,a)))
            if a not in o_moves:
                o_moves.append(a)
        return v


    # Given a state s
    # Max player picks action a in actions(s) to get highest value of minvalue(result(s,a))
    if player(board) == X:
        print("move X")
        print("x_count: ",x_count)
        score = maxvalue(board)
        # print("score: ",score)
        if score == -1:
            # print("o won")
            # print(o_moves)
            return o_moves.pop(0)
        if score == 1:
            # print("x won")
            # print(x_moves)
            return x_moves.pop(0)
        if score == 0 and moves_left == True:
            # print("Tied")
            # print(o_moves)
            return o_moves.pop(0)
        if score == 0 and moves_left == False:
            print("Tied")
            return None

    # Min player picks action a in actions(s) to get lowest value of maxvalue(result(s,a))
    if player(board) == O:
        print("move O")
        print("o_count: ",o_count)
        score = minvalue(board)
        # print("score: ",score)
        if score == -1:
            # print("o won")
            # print("AI moves: ",o_moves)
            return o_moves.pop(0)
        elif score == 1:
            # print("x won")
            # print(x_moves)
            return x_moves.pop(0)
        elif score == 0 and moves_left == True:
            # print("tie")
            # print(o_moves)
            return o_moves.pop(0)
        elif score == 0 and moves_left == False:
            # print("Tied")
            return None
    


   