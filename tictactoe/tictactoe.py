"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None

turn_counter = 0

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
    # raise NotImplementedError
    
    if board == initial_state():
        return X
    else:
        count_x = sum([row.count(X) for row in board])
        count_o = sum([row.count(O) for row in board])

        if count_x <= count_o:
            return X
        else:
            return O

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    # raise NotImplementedError
    return [(i,j) for i in range(len(board)) for j in range(len(board[0])) if board[i][j] == EMPTY] 


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # raise NotImplementedError
    modified_board = copy.deepcopy(board)
    if action in actions(board):
        modified_board[action[0]][action[1]] = player(board)
        return modified_board
    else:
        raise InvalidActionError()


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    
    for i in range(len(board)):
        if (board[i][0] == board[i][1] and board[i][1] == board[i][2]) and board[i][0] != EMPTY:
            return board[i][0]
        elif (board[0][i] == board[1][i] and board[1][i] == board[2][i]) and board[0][i] != EMPTY:
            return board[0][i]
        elif (board[0][0] == board[1][1] and board[1][1] == board[2][2]) or (board[2][0] == board[1][1] and board[1][1] == board[0][2]):
            if board[1][1] != EMPTY:
                return board[1][1]

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    return (winner(board) != None) or (sum([row.count(None) for row in board]) == 0)


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    winning_player = winner(board)
    if winning_player == X:
        return 1
    elif winning_player == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    # raise NotImplementedError

    player_sigil = player(board)
    myutility = []
    myactions = actions(board)
    if player_sigil == X:
        for action in myactions:
            myutility.append(minvalue(result(board,action)))
        idx = myutility.index(max(myutility))

    else:
        for action in myactions:
            myutility.append(maxvalue(result(board,action)))
        idx = myutility.index(min(myutility))
    return myactions[idx]

def minvalue(board):
    if terminal(board):
        return utility(board)
    v = 1e12

    for action in actions(board):
        v = min(v, maxvalue(result(board,action)))
    return v

def maxvalue(board):
    if terminal(board):
        return utility(board)
    v = -1e12
    for action in actions(board):
        v = max(v, minvalue(result(board,action)))
    return v

# cutom exception if an action is invalid
class InvalidActionError(Exception):
    def __init__(self):
        print("The action is invalid")