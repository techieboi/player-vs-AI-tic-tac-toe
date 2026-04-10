"""
Tic Tac Toe Player
"""

import math
import copy

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
    countx = 0
    counto = 0

    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == X:
                countx += 1
            if board[row][col] == O:
                counto += 1

    if countx > counto:
        return O
    else:
        return X



def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possibleActions = set()

    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == EMPTY:
                possibleActions.add((row, col))

    return possibleActions



def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise Exception("Invalid action")

    row, col = action
    copyBoard = copy.deepcopy(board)

    copyBoard[row][col] = player(board)
    return copyBoard



def checkrow(board, player):
    for row in range(len(board)):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            return True
    return False



def checkcol(board, player):
    for col in range(len(board)):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            return True
    return False


def checkdiag(board, player):
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if checkrow(board, X) or checkcol(board, X) or checkdiag(board, X):
        return X
    if checkrow(board, O) or checkcol(board, O) or checkdiag(board, O):
        return O
    return None



def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True

    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == EMPTY:
                return  False
    return True

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def max_value(board):
    if terminal(board):
        return utility(board)

    v = -math.inf
    bestAction = None
    for action in actions(board):
        minVal, _ = min_value(result(board, action))
        if minVal > v:
            v = minVal
            bestAction = action
    return v, bestAction


def min_value(board):
    if terminal(board):
        return utility(board)

    v = math.inf
    bestAction = None
    for action in actions(board):
        maxVal, _ = max_value(result(board, action))
        if maxVal < v:
            v = maxVal
            bestAction = action
    return v, bestAction




def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    if player(board) == X:
        _, optimalAction = max_value(board)
        return optimalAction
    else:
        _, optimalAction = min_value(board)
        return optimalAction


