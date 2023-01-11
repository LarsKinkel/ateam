import numpy as np

class Grid:
    """
    Grid object that states the size of the board.

    Attributes:
        vehicles: vehicles that are on the grid
        dimension: dimesion of the board
    """
    def __init__(self, dimension):
        self.grid = np.zeros((dimension, dimension))

    def add_vehicle(self, vehicle):
        if vehicle.orientation == 'H':
            self.grid[vehicle.row - 1][vehicle.col - 1: vehicle.col - 1 + vehicle.length] = vehicle.name
        elif vehicle.orientation == 'V':
            self.grid[vehicle.row - 1: vehicle.row - 1 + vehicle.length, vehicle.col - 1] = vehicle.name

    def __str__(self):
        return str(self.grid)
