import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap, BoundaryNorm
import numpy as np

# Make a 9x9 grid...
# nrows, ncols = 6,6
# # board = np.zeros(nrows*ncols)
# board = [[ 0,  1,  1,  2,  2,  2],
#  [ 0,  3,  3,  5,  4,  4],
#  [24, 24,  7,  5,  0,  9],
#  [ 6,  6,  7,  8,  8,  9],
#  [11,  0, 12,  0, 10, 10],
#  [11,  0, 12,  0,  0,  0]]

# # Set every other cell to a random number (this would be your data)
# board[::2] = np.random.random(nrows*ncols // 2 + 1)
# board[::2] = np.random.random(1)

# Reshape things into a 6x6 grid.
# board = board.reshape((nrows, ncols))


def visualize_grid(board: np.ndarray, dimension: int):
    """ Function to visualize the grid.

    Attributes:
        board (np.ndarray[tuple[str,str,int]]): 2d array containing tuples of U1,U1,i
        dimension (int): dimensions of board
    """
    norm = BoundaryNorm(
        np.unique(board['name']),
        len(np.unique(board['name'])) - 1)

    # For a 6x6 grid
    if dimension == 6:
        cmap = ListedColormap([
            'white',
            'khaki',
            'lightblue',
            'lightgreen',
            'orange',
            'blue',
            'purple',
            'lime',
            'grey',
            'crimson',
            'yellow',
            'brown',
            'darkgreen',
            'red'
        ])
    # For a 9x9 grid
    elif dimension == 9:
        cmap = ListedColormap([
            'white',
            'khaki',
            'lightblue',
            'lightgreen',
            'orange',
            'blue',
            'purple',
            'lime',
            'grey',
            'crimson',
            'yellow',
            'brown',
            'darkgreen',
            'darkslategrey',
            'magenta',
            'pink',
            'olivedrab',
            'steelblue',
            'navy',
            'lavender',
            'salmon',
            'sandybrown',
            'maroon',
            'indianred',
            'darkolivegreen',
            'cyan',
            'red'
        ])

    row_labels = range(1, dimension + 1)
    col_labels = range(1, dimension + 1)

    plt.imshow(board['name'], cmap=cmap, norm=norm)
    plt.xticks(range(dimension), col_labels)
    plt.yticks(range(dimension), row_labels)
    plt.show()
