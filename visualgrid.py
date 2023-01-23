import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap, BoundaryNorm
import matplotlib.animation as animation
import numpy as np
from typing import List

def visualize(boards: List[np.ndarray], dimension: int, showplot: bool = True, saveplot: bool = False, filename: str = 'Solution'):
    """ Function to make an animation of the grid.

    Attributes:
        boards (List[np.ndarray]): List of 2d arrays containing the position of the grids
        dimension (int): dimensions of board
    """
    norm = BoundaryNorm(
        np.unique(boards[0]),
        len(np.unique(boards[0]) - 1))

    # For a 6x6 grid
    if dimension == 6:
        colors = [
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
        ]
        cmap = ListedColormap(colors)
    # For a 9x9 grid
    elif dimension == 9:
        colors = [
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
        ]
        cmap = ListedColormap(colors)
    else:
        colors = [
            'white',
            'navy',
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
            'khaki',
            'lavender',
            'salmon',
            'sandybrown',
            'maroon',
            'indianred',
            'darkolivegreen',
            'cyan',
            'darkkhaki',
            'gold',
            'indigo',
            'deepskyblue',
            'chocolate',
            'lightcyan',
            'dodgerblue',
            'fuchsia',
            'silver',
            'darkorange',
            'deeppink',
            'teal',
            'mediumspringgreen',
            'mediumseagreen',
            'aqua',
            'lemonchiffon',
            'lawngreen',
            'slateblue',
            'papayawhip',
            'red'
        ]
        cmap = ListedColormap(colors)

    # Set up figure
    fig = plt.figure(figsize=(8,8))

    # Plot frames
    ims = [[plt.imshow(board, vmin=0, vmax=len(colors), cmap=cmap, norm = norm, animated=True)] for board in boards]

    
    row_labels = range(1, dimension + 1)
    col_labels = range(1, dimension + 1)

    plt.xticks(range(dimension), col_labels)
    plt.yticks(range(dimension), row_labels)
    plt.tight_layout()
    

    ani = animation.ArtistAnimation(fig, ims, interval=500, blit=True, repeat_delay=1000)

    if saveplot:
        ani.save(filename + '.gif', writer=animation.PillowWriter(fps=20))

    if showplot:
        plt.show()
