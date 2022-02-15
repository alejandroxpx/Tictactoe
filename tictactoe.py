"""
Tic Tac Toe Player
"""

import math, copy, random
from sqlite3 import OptimizedUnicode

from numpy import Infinity

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    # """
    # return [[EMPTY, EMPTY, EMPTY],
    #         [EMPTY, EMPTY, EMPTY],
    #         [EMPTY, EMPTY, EMPTY]]

    return  [[EMPTY, X, O],
            [EMPTY, EMPTY, EMPTY],
            [X, EMPTY, O]]

    # return  [[X, X, O],
    #         [O, O, EMPTY],
    #         [X, EMPTY, EMPTY]]

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
    if board == initial_state():
        return X
    elif xcount > ocount:
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
    # if terminal(board) == True:
    #     return None
    return moves

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # if action == None:
        # raise ValueError("No more actions")

    board_copy = copy.deepcopy(board)
    for i in range(3):
        for j in range(3):
            if i == action[0] and j == action[1]:
                board_copy[i][j] = player(board)
    # print("",board_copy[0],"\n",board_copy[1],"\n",board_copy[2],"\n")
    return board_copy

def moves_left(board):
    """
    Returns True if there are any moves left to play, else returns False.
    """
    for i in range(3):
        for j in range(3):
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
        return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # Game over
    if winner(board) == X or winner(board) == O or moves_left(board) == False:
        return True
    # Game in progress
    else: 
        return False
   
def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O: 
        return -1
    elif moves_left(board) == False: 
        return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    xmoves = []
    optimal_X = []
    omoves = []
    optimal_O = []
    counter = 0

    def maxvalue(state):
        v = -10
        if terminal(state):
            # print("Terminal state: \n",state[0],"\n",state[1],"\n",state[2],"\n")
            # print("Terminal: ",terminal(state)," ","Utilty value: ",utility(state))
            return utility(state)#-1,0,or 1
        for action in actions(state):
            # print("current action: ",action,"\nboard: \n",  state[0],"\n",state[1],"\n",state[2],"\n")
            v = max(v, minvalue(result(state,action)))
            if v == -1:
                optimal_O.append(action)
                # print("o won")
            elif v == 1:
                # print("x won")
                optimal_X.append(action)
            elif v == 0:
                optimal_O.append(action)
                # print("tied")       
        return v

    def minvalue(state):
        v = 10
        if terminal(state):
            # print("Terminal state: \n",state[0],"\n",state[1],"\n",state[2],"\n")
            # print("terminal: ",terminal(state)," ","utilty value: ",utility(state))
            return utility(state)
        for action in actions(state):
            # print("Current action: ",action,"\nboard: \n", state[0],"\n",state[1],"\n",state[2],"\n")
            v = min(v, maxvalue(result(state,action)))
            if v == -1:
                optimal_O.append(action)
                # print("o won")
            elif v == 1:
                # print("x won")
                optimal_X.append(action)
            elif v == 0:
                optimal_O.append(action)
                # print("tied")       
        return v 

    scores_x = []
    scores_o = []
    if player(board) == X:
        score = maxvalue(board)
        print("score: ",score)
        if score == -1:
            return optimal_O[0]
        if score == 0:
            return optimal_O[0]
        if score == 1:
            return optimal_X[0]
    elif player(board) == O:
        score = minvalue(board)
        print("score: ",score)
        if score == -1:
            return optimal_O[0]
        if score == 0:
            return optimal_O[0]
        if score == 1:
            return optimal_X[0]
