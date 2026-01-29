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
    count_x = 0
    count_o = 0

    for row in board:
        for cell in row:
            # Count the number of turns played by each player
            if cell == X:
                count_x += 1
            elif cell == O:
                count_o += 1

    # Since X starts
    if count_x == 0 and count_o == 0:
        return X
    elif count_x > count_o:
        return O
    # "Minus equal to" since X started the game
    elif count_o >= count_x:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    n_row = -1

    for row in board:
        n_row += 1
        n_cell = -1
        for cell in row:
            n_cell += 1
            # If the cell is empty I add the cell to the set of the
            # possible actions
            if cell == EMPTY:
                action = (n_row, n_cell)
                actions.add(action)

    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board = copy.deepcopy(board)

    # Check if the action is valid
    if board[action[0]][action[1]] != EMPTY or (action[0] or action[1]) > 2 or (action[0] or action[1]) < 0:
        raise ValueError

    # Check whose turn it is and then change the board's copy
    if player(board) == X:
        new_board[action[0]][action[1]] = X
        return new_board
    else:
        new_board[action[0]][action[1]] = O
        return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check horizontally
    for row in board:
        count_x = 0
        count_o = 0
        for cell in row:
            if cell == X:
                count_x += 1
            elif cell == O:
                count_o += 1
        if count_x == 3:
            return X
        elif count_o == 3:
            return O

    # Check diagonally
    if board[0][0] == board[1][1] == board[2][2] == X or board[2][0] == board[1][1] == board[0][2] == X:
        return X
    elif board[0][0] == board[1][1] == board[2][2] == O or board[2][0] == board[1][1] == board[0][2] == O:
        return O

    # Check vertically
    for col in range(3):
        vertical_x = 0
        vertical_o = 0
        for row in range(3):
            if board[row][col] == X:
                vertical_x += 1
            elif board[row][col] == O:
                vertical_o += 1

            if vertical_x == 3:
                return X
            elif vertical_o == 3:
                return O

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) == X or winner(board) == O:
        return True
    # Check if the game is finished and it's a tie
    elif winner(board) == None:
        # Check all the cells
        for col in board:
            for cell in col:
                # If I find an empty cell then the game is not over
                if cell == EMPTY:
                    return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    # Utility 1 if X (the maximizer) wins
    if winner(board) == X:
        return 1
    # Utility -1 if O (the minimizer) wins
    elif winner(board) == O:
        return -1
    # If it's a tie
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    if player(board) == X:
        optimal = max_value(board)
        # Return the second value (the move)
        return optimal[1]
    elif player(board) == O:
        optimal = min_value(board)
        return optimal[1]


def min_value(board):

    if terminal(board):
        return utility(board), None

    v_ = float('inf')

    for action in actions(board):
        # Assing to max the value returned by max function
        max = max_value(result(board, action))
        # Assign to v the min value between v_ and max
        v = min(v_, max[0])

        # If I find a v which is less than v_ then I assign
        # v to v_ and register the action
        if v < v_:
            optimal = action
            v_ = v

    return v, optimal


def max_value(board):

    if terminal(board):
        return utility(board), None

    v_ = float('-inf')

    for action in actions(board):
        min = min_value(result(board, action))
        v = max(v_, min[0])

        if v > v_:
            optimal = action
            v_ = v

    return v, optimal
