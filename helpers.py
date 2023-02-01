import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap, BoundaryNorm
import matplotlib.animation as animation
import numpy as np
from typing import List
from Code.Algorithms.randomise import Randomalgorithm

# from visualgrid import visual
import csv

def write_to_output(moves, filename):
    # Keep track of the moves in the outputfile
    with open(filename + ".csv", 'w+') as f:
        dw = csv.DictWriter(f, delimiter=',', fieldnames= ["car", "move"])
        dw.writeheader()
        writer = csv.writer(f)

        for move in moves:
            if move[0] > 26:
                if move[0] == 99:
                    namecar = chr(88)
                else:
                    namecar = "A" + chr(int(move[0]) - 26 + 64)
            else:
                namecar = chr(int(move[0]) + 64)

            writer.writerow((namecar, move[1]))

    print(f"The moves has been written to '{filename}.csv'")

def visual(boards: List[np.ndarray], dimension: int, showplot: bool = True, saveplot: bool = False, filename: str = 'Solution'):
    """ Function to make an animation of the grid.

    Attributes:
        boards (List[np.ndarray]): List of 2d arrays containing the position of the grids
        dimension (int): dimension of board
    """

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

    norm = BoundaryNorm(np.unique(boards[0]), len(np.unique(boards[0]) - 1))

    # Set up figure
    fig = plt.figure(figsize=(8,8))

    # Plot frames
    ims = [[plt.imshow(board, cmap=cmap, norm = norm, animated=True)] for board in boards]


    row_labels = range(1, dimension + 1)
    col_labels = range(1, dimension + 1)

    plt.xticks(range(dimension), col_labels)
    plt.yticks(range(dimension), row_labels)
    plt.tight_layout()


    ani = animation.ArtistAnimation(fig, ims, interval=500, blit=True, repeat_delay=500)

    if saveplot:
        ani.save(filename + '.gif', writer=animation.PillowWriter(fps=20))

    if showplot:
        plt.show()



def solution_visual(start_grid, moves, filename):
    """
    Creates an animation of the given start grid and the moves
    pre: Grid is an object, moves is a list of moves in tuple form (car, move) and the filename is a string
    post: Creates and saves the animation
    """
    for move in moves:
        for vehicle in start_grid.vehicles:
            if vehicle.name == move[0]:
                start_grid.move_vehicle(vehicle.row - 1, vehicle.col - 1, move[1])
                start_grid.update_grid()

    visual(start_grid.visual, start_grid.dim, saveplot=True, filename=filename)


def get_goal_state(grid):
    """
    Pre: grid object
    Post: returns a final state of the inserted grid object
    """

    vehicles = grid.vehicles
    Algorithm = Randomalgorithm(grid, vehicles)
    goalstate = Algorithm.solve()[2]
    return goalstate


def get_manhattan_distance(vehicle, goal_position):
    """
    Pre: input a vehicle and its goal position
    Post: returns the manhattan distance of the vehicle towards his goal state
    """

    for vehicle_goal in goal_position.vehicles:
        if vehicle_goal.name == vehicle.name:
            xdist = abs(vehicle_goal.col - vehicle.col)
            ydist = abs(vehicle_goal.row - vehicle.row)

            ManDist = xdist + ydist

            return ManDist


def heuristics(grid, type, goalstate=None):
    """
    Heuristic function that calculates the heuristic value of a grid, depending
    on the heuristic that one wants to use (type)

    Pre: needs a grid, and a type (1-3), for heuristic 3, needs a goalstate.
    Post: returns a heuristic score which is an integer value, for the grid inserted
    """

    # Heuristic 1: Distance red car to exit
    if type == 1:
        heuristic = 0

        # find column red car
        for vehicle in grid.vehicles:
            if vehicle.name == 99:
                redcar_col = vehicle.col
                break

        # determine final column depending on gridsize
        final_col = grid.dim - 1

        # add the distance of the redcar to the final column to the heuristic
        heuristic += final_col - redcar_col

        return heuristic

    # Heuristic 2: Nr of cars blocking the exit way of the red car
    elif type == 2:
        heuristic = 0

        # find row and col of red car
        for vehicle in grid.vehicles:
            if vehicle.name == 99:
                redcar_row = vehicle.row
                redcar_col = vehicle.col
                break

        for i in range(redcar_col + 1, grid.dim):
            if grid.grid[redcar_row - 1][i] != 0:
                heuristic += 1

        return heuristic

    # Heuristic 3: Manhattan Distance to goal
    elif type == 3:
        heuristic = 0

        for vehicle in grid.vehicles:
            ManDist = get_manhattan_distance(vehicle, goalstate)
            heuristic += ManDist

        return heuristic
