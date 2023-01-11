import numpy as np

class Grid:
    """
    Grid object that states the size of the board.

    Attributes:
        vehicles: vehicles that are on the grid
        dimension: dimesion of the board
    """
    def __init__(self, dimension):
        self.grid = np.zeros(dimension, dimension)

    def add_vehicle(self, vehicle):
        pass

    def __str__(self):
        return self.grid
