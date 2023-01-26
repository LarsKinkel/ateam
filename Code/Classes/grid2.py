import numpy as np
from Code.Classes.vehicle import *
import csv

class Grid:
    """
    Grid object that states the size of the board
    and stores the vehicles on the board.

    Attributes:
        vehicles: vehicles that are on the grid
        dimension: dimesion of the board
    """
    def __init__(self, dimension: int, vehicles):
        self.grid = np.zeros((dimension, dimension))
        self.vehicles = vehicles
        self.dim = dimension
        self.visual = []
        self.depth = 0
        self.stored_moves = {}

        for vehicle in self.vehicles:
            if vehicle.orientation == 'H':
                self.grid[vehicle.row - 1][vehicle.col - 1: vehicle.col - 1 + vehicle.length] = vehicle.name
            elif vehicle.orientation == 'V':
                self.grid[vehicle.row - 1: vehicle.row - 1 + vehicle.length, vehicle.col - 1] = vehicle.name

        self.visual.append(self.grid)

        self.solvecol = self.dim - 1


    def move_possible(self, row: int, col: int, delta: int):
        """
        Function that checks if a move is possible

        Pre:    Insert the row, column and delta of the move
        Post:   Returns True if move is possible, returns False is a move is not move_possible,
                returns None if the car is not found.
        """
        for vehicle in self.vehicles:
            if vehicle.row - 1 == row and vehicle.col - 1 == col:
                if vehicle.orientation == 'H':
                    new_col = col + delta
                    if delta == -1:
                        # Validate grid borders
                        if new_col < 0 or self.grid[vehicle.row - 1, vehicle.col - 2] != 0 :
                            return False
                        return True
                    elif delta == 1:
                        if new_col + vehicle.length > self.dim or self.grid[vehicle.row - 1, vehicle.col - 1 + vehicle.length] != 0:
                            return False
                        return True
                elif vehicle.orientation == 'V':
                    new_row = row - delta
                    if delta == -1:
                        # Validate that we are not mounting another vehicle:
                        if new_row + vehicle.length > self.dim or self.grid[vehicle.row - 1 + vehicle.length, vehicle.col - 1] != 0:
                            return False
                    elif delta == 1:
                        # Validate grid borders
                        if new_row < 0 or self.grid[vehicle.row - 2, vehicle.col - 1] != 0:
                            return False
                        return True
                    return True


    def move_vehicle(self, row: int, col: int, delta:int):
        """
        Function that changes the row and column of a vehicle object, according to a move.

        Pre:    Insert the row, column and delta of the move
        Post:   After running the function, the row and column of the vehicle
                object are changed according to the move. Every move is written in
                the output.csv file.
        """

        # Loop through vehicles, and find the vehicle that is on the inserted coordinates
        for vehicle in self.vehicles:
            if vehicle.row - 1 == row and vehicle.col - 1 == col:
                # Distinguish cases for different orientation of the vehicle
                # Use set_new_... method to assign new row or col
                if vehicle.orientation == 'H':
                    new_col = col + delta
                    vehicle.set_new_col(new_col + 1)
                elif vehicle.orientation == 'V':
                    new_row = row - delta
                    vehicle.set_new_row(new_row + 1)
                # Keep track of the moves in the outputfile
                # with open('output.csv', 'a') as f:
                #     writer = csv.writer(f)
                #     if vehicle.name == 99:
                #         name = 24
                #         namecar = chr(int(name)+64)
                #     else:
                #         namecar = chr(int(vehicle.name)+64)
                #     writer.writerow((namecar, delta))


    def store_move(self, row, col, delta):

        for vehicle in self.vehicles:
            if vehicle.row - 1 == row and vehicle.col - 1 == col:
                if vehicle.name == 99:
                    name = 24
                    namecar = chr(int(name)+64)
                else:
                    namecar = chr(int(vehicle.name)+64)

                self.past_moves[namecar] = delta


    def update_grid(self):
        """
        Method that can be used to update the grid after a move has been made.

        Pre:    Using the grid and vehicles list of the object.
        Post:   Grid is updated if a move has been made according to the new
                vehicles list.
        """
        self.grid = np.zeros((self.dim, self.dim))
        for vehicle in self.vehicles:
            if vehicle.orientation == 'H':
                self.grid[vehicle.row - 1][vehicle.col - 1: vehicle.col - 1 + vehicle.length] = vehicle.name
            elif vehicle.orientation == 'V':
                self.grid[vehicle.row - 1: vehicle.row - 1 + vehicle.length, vehicle.col - 1] = vehicle.name

        self.visual.append(self.grid)

    def is_solved(self):
        for vehicle in self.vehicles:
            if vehicle.name == 99:
                return vehicle.col == self.solvecol



    def __str__(self):
        return str(self.grid)

    # def __eq__(self, other):
    #     return self.grid == other.grid
    #
    # def __ne__(self, other):
    #     return not self.__eq__(other)


def setupgrid(game: int):
    """
    Makes the grid object for the given game.

    Pre:    Number of the game to be solved.
    Post:   Grid object is returned that contains the chosen game.
    """
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
