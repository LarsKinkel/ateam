import numpy as np
from Code.Classes.vehicle import *
import csv

class Grid:
    """
    Grid object that states the size of the board.

    Attributes:
        vehicles: vehicles that are on the grid
        dimension: dimesion of the board
    """
    def __init__(self, dimension, vehicles):
        self.grid = np.zeros((dimension, dimension))
        self.vehicles = vehicles
        self.dim = dimension

        for vehicle in self.vehicles:
            if vehicle.orientation == 'H':
                self.grid[vehicle.row - 1][vehicle.col - 1: vehicle.col - 1 + vehicle.length] = vehicle.name
            elif vehicle.orientation == 'V':
                self.grid[vehicle.row - 1: vehicle.row - 1 + vehicle.length, vehicle.col - 1] = vehicle.name

    def move_possible(self, row, col, delta):
        for vehicle in self.vehicles:
            if vehicle.row - 1 == row and vehicle.col - 1 == col:
                if vehicle.orientation == 'H':
                    new_col = col + delta
                    if delta == -1:

                        # Validate grid borders
                        if new_col < 0 or self.grid[vehicle.row - 1, vehicle.col - 2] != 0 :
                            return False

                        return True

                    elif new_col + vehicle.length > self.dim or self.grid[vehicle.row - 1, vehicle.col + vehicle.length] != 0:
                        return False
                    return True

                elif vehicle.orientation == 'V':
                    new_row = row - delta

                    # Validate grid borders
                    if new_row < 0 or new_row + vehicle.length > self.dim:
                        return False

                    # validate that we are not mounting another vehicle: # TODO:
                    if self.grid[vehicle.row - 2, vehicle.col - 1] != 0 or self.grid[vehicle.row + vehicle.length, vehicle.col] != 0:
                        return False

                return True


    def move_vehicle(self, row, col, delta):
        for vehicle in self.vehicles:
            if vehicle.row - 1 == row and vehicle.col - 1 == col:
                if vehicle.orientation == 'H':
                    new_col = col + delta
                    vehicle.set_new_col(new_col + 1)



                elif vehicle.orientation == 'V':
                    new_row = row - delta
                    vehicle.set_new_row(new_row + 1)



                with open('output.csv', 'a') as f:
                    writer = csv.writer(f)
                    namecar = chr(int(vehicle.name)+64)
                    writer.writerow((namecar, delta))


    def update_grid(self):
        self.grid = np.zeros((self.dim, self.dim))
        for vehicle in self.vehicles:
            if vehicle.orientation == 'H':
                self.grid[vehicle.row - 1][vehicle.col - 1: vehicle.col - 1 + vehicle.length] = vehicle.name
            elif vehicle.orientation == 'V':
                self.grid[vehicle.row - 1: vehicle.row - 1 + vehicle.length, vehicle.col - 1] = vehicle.name

        return self.grid



    def __str__(self):
        return str(self.grid)


def setupgrid(game: int):
    if game == 1:
        vehicles = load_vehicles("Rushhour6x6_1.csv")
        grid = Grid(6, vehicles)
        return grid

    elif game == 2:
        vehicles = load_vehicles("Rushhour6x6_2.csv")
        grid = Grid(6, vehicles)
        return grid

    elif game == 3:
        vehicles = load_vehicles("Rushhour6x6_3.csv")
        grid = Grid(6, vehicles)
        return grid

    elif game == 4:
        vehicles = load_vehicles("Rushhour9x9_4.csv")
        grid = Grid(9, vehicles)
        return grid

    elif game == 5:
        vehicles = load_vehicles("Rushhour9x9_5.csv")
        grid = Grid(9, vehicles)
        return grid

    elif game == 6:
        vehicles = load_vehicles("Rushhour9x9_6.csv")
        grid = Grid(9, vehicles)
        return grid

    elif game == 7:
        vehicles = load_vehicles("Rushhour12x12_7.csv")
        grid = Grid(12, vehicles)
        return grid
