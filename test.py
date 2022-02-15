from tictactoe import initial_state
from tictactoe import winner
from tictactoe import terminal
from tictactoe import moves_left
from tictactoe import actions
from tictactoe import result
from tictactoe import moves_left
from tictactoe import utility
from tictactoe import player
from tictactoe import minimax

X = "X"
O = "O"
EMPTY = None

# board = [[EMPTY,    O,      O],
#           [X,       X,      O],
#          [X,      EMPTY,  X]]

# board = [[X, EMPTY, EMPTY],
#             [EMPTY, EMPTY, EMPTY],
#             [EMPTY, EMPTY, EMPTY]]
board =    [[X,     O,      X],
            [O,     O,      EMPTY],
            [EMPTY, X,      X]]

# board =    [[X, X, O],
#             [O, O, O],
#             [X, X, O]]

# print("         Minimax             ")
print("optimal Move ... ",minimax(board))

# # print("         Player             ")
# print("Current player is. ",player(board))

# # print("         Actions             ")
# print("Actions available from board. ",actions(board))

# # print("         Result             ")
# print("Resulting board from move. ",result(board, (0,0)))


# # print("         Winner             ")s
# print("Is there a winner? ",winner(board))

# # print("         Terminal             ")
# print("Is the game a terminal board? ",terminal(board))

# # print("         Moves_left             ")
# print("Are there any moves left? ", moves_left(board))

# print("         Utility             ")
# print("Utility of current board. ",utility(board))

