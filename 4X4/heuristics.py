import global_vars
import numpy as np
from global_vars import DIMENSION


def heuristic_value(test_move: tuple, game_state: np.ndarray):
    """
    Calculate a heuristic score.
    + 100 for EACH 3-in-a-line (with 1 empty cell)
    +  10 for EACH two-in-a-line (with 2 empty cells)
    +   1 for EACH one-in-a-line (with 3 empty cells)
    Negate scores for opponent positions
    """
    i = test_move[0]
    j = test_move[1]
    player = game_state[i][j]

    # Test row
    total = 0
    for y in range(DIMENSION):
        if game_state[i][y] == player:
            total += 1
        elif game_state[i][y] != 0:
            total = 0
            break
    if total == DIMENSION - 1:
        row_score = 100
    elif total == DIMENSION - 2:
        row_score = 10
    elif total > 0:
        row_score = 1
    else:
        row_score = 0

    # Test column
    total = 0
    for x in range(DIMENSION):
        if game_state[x][j] == player:
            total += 1
        elif game_state[x][j] != 0:
            total = 0
            break
    if total == DIMENSION - 1:
        col_score = 100
    elif total == DIMENSION - 2:
        col_score = 10
    elif total > 0:
        col_score = 1
    else:
        col_score = 0

    # Test diagonals
    total = 0
    if i == j:
        for x in range(DIMENSION):
            if game_state[x][x] == player:
                total += 1
            elif game_state[x][x] != 0:
                total = 0
                break
    elif i == DIMENSION - j - 1:
        for x in range(DIMENSION):
            y = DIMENSION - x - 1
            if game_state[x][y] == player:
                total += 1
            elif game_state[x][y] != 0:
                total = 0
                break
    if total == DIMENSION - 1:
        diagonal_score = 100
    elif total == DIMENSION - 2:
        diagonal_score = 10
    elif total > 0:
        diagonal_score = 1
    else:
        diagonal_score = 0

    # Return heuristic score
    return row_score + col_score + diagonal_score
