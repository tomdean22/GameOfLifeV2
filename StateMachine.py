from enum import Enum, auto
import numpy as np

ROWS, COLUMNS = 10, 10

class State(Enum):
    DEAD = auto()   
    ALIVE = auto()


class Trigger(Enum):
    BADPOPULATION = lambda i,j,b: count_neighbors(i,j,b) < 2 or count_neighbors(i,j,b) > 3
    JUSTRIGHT = lambda i,j,b: count_neighbors(i,j,b) == 3


# if a cell is dead it can only be resurrected
# if a cell is alive it can only be killed
# use a trigger to check the condition
rules = {
        State.DEAD:  (Trigger.JUSTRIGHT, State.ALIVE),
        State.ALIVE: (Trigger.BADPOPULATION, State.DEAD)
    }


def count_neighbors(row, column, board):
    count = 0
    for i in [-1,0,1]:
        for j in [-1,0,1]:
            if i is 0 and j is 0:
                pass
            else:
                try:
                    if board[row+i][column+j] == State.ALIVE:
                        count += 1
                except IndexError:
                    # What to do with neighbor cells outside the grid?
                    pass
    return count

def update_board(current_gen):
    """ current_gen is a 2D numpy array """
    next_gen = np.full((ROWS, COLUMNS), State.DEAD)
    for row in range(ROWS):
        for column in range(COLUMNS):
            state = current_gen[row][column]
            if rules[state][0](row, column, current_gen):
                next_gen[row][column] = rules[state][1]
            else:
                next_gen[row][column] = state
    return next_gen

def initialize_board_from_seed(seed=None):
    """ seed is a list of coordinate pairs representing cells (e.g. [(3,4),(5,6)]) """
    board = np.full((ROWS, COLUMNS), State.DEAD)
    for i,j in seed:
        board[i][j] = State.ALIVE
    return board


# JUST FOR DEV
def live_cells(board):
    alive = []
    for row in range(ROWS):
        for column in range(COLUMNS):
            if board[row][column] == State.ALIVE:
                alive.append((row,column))
    return alive



if __name__ == '__main__':
    print_live_cells = lambda board: print(' '.join([str(i) for i in live_cells(board)]))
    seed = [(5,3),(5,4),(5,5)]

    board = initialize_board_from_seed(seed)
    print_live_cells(board) # output: (5, 3) (5, 4), (5, 5)

    board = update_board(board)
    print_live_cells(board) # output: (4, 4) (5, 4), (6, 4)
    

