import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import numpy as np

# Make a 9x9 grid...
nrows, ncols = 6,6
# board = np.zeros(nrows*ncols)
board = [[ 0,  1,  1,  2,  2,  2],
 [ 0,  3,  3,  5,  4,  4],
 [24, 24,  7,  5,  0,  9],
 [ 6,  6,  7,  8,  8,  9],
 [11,  0, 12,  0, 10, 10],
 [11,  0, 12,  0,  0,  0]]

# # Set every other cell to a random number (this would be your data)
# board[::2] = np.random.random(nrows*ncols // 2 + 1)
# board[::2] = np.random.random(1)

# Reshape things into a 6x6 grid.
# board = board.reshape((nrows, ncols))

cmap = ListedColormap(['w',
                        'k',
                        'lightblue',
                        'lightgreen',
                        'orange',
                        'b',
                        'purple',
                        'g',
                        'grey',
                        'beige',
                        'yellow',
                        'brown',
                        'darkgreen',
                        # 'black',
                        # 'cyan',
                        # 'darkblue',
                        # 'turquoise',
                        'r'])

row_labels = range(1,7)
col_labels = range(1,7)
plt.imshow(board, cmap = cmap)
plt.xticks(range(ncols), col_labels)
plt.yticks(range(nrows), row_labels)
plt.show()
