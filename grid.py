import numpy as np
from vehicle import *


class Grid:
    """
    Grid object that states the size of the board.

    Attributes:
        vehicles: vehicles that are on the grid
        dimension: dimesion of the board
    """

    def __init__(self, dimension: int):
        # Grid is a 2d array containing tuple[int, str, int]
        # Data type source: https://numpy.org/doc/stable/reference/arrays.dtypes.html#index-6:~:text=%27U%27-,Unicode%20string,-%27V%27
        self.dt = np.dtype(
            [('name', 'i'), ('orientation', 'U1'), ('length', 'i')]
        )
        self.grid = np.zeros((dimension, dimension), dtype=self.dt)
        self.dim = dimension

    # Misschien moeten deze methods (add vehicle, move) in de Rush Hour class, want daar programmeren wij het echte spel

    def add_vehicle(self, vehicle: Vehicle):
        """ Function to add a vehicle on the grid with their
        specific properties (vehicle number, orientation and length)

        Attributes:
            vehicle (Vehicle): 
        """
        data = (vehicle.name, vehicle.orientation, vehicle.length)
        if vehicle.orientation == 'H':
            self.grid[vehicle.row - 1, vehicle.col -
                      1: vehicle.col - 1 + vehicle.length] = data
        elif vehicle.orientation == 'V':
            self.grid[vehicle.row - 1: vehicle.row - 1 +
                      vehicle.length, vehicle.col - 1] = data

    def get_vehicle(self, row: int, col: int):
        """ Function to return if there is a vehicle on a given coordinate"""
        return self.grid[row, col]

    def move_vehicle(self, col: int, row: int, delta: int):
        """ Function to move a vehicle on the grid

        Attributes:
            vehicle: a tuple containing the name, orientation and length
            delta: the number of spots to move the vehicle 
        """
        # Copy so we don't lose the vehicle properties when overriding
        vehicle = self.get_vehicle(row, col).copy()
        if vehicle is None:
            return False

        # If vehicle is horizontal
        if vehicle[1] == 'H':
            new_col = col + delta
            # Validate grid borders
            if new_col < 0 or new_col + vehicle[2] > self.dim:
                return False
            # Validate that we are not mounting another vehicle
            if np.setdiff1d([0, vehicle['name']], self.grid[row, new_col:new_col+vehicle[2]]['name']).size != 0:
                return False
            # Set the old vehicle location as empty
            self.grid[row, col:col+vehicle[2]] = (0, '', 0)
            # Move the vehicle to the new location
            self.grid[row, new_col:new_col+vehicle[2]] = vehicle
        elif vehicle[1] == 'V':
            new_row = row + delta
            # Validate grid borders
            if new_row < 0 or new_row + vehicle[2] > self.dim:
                return False
            # Validate that we are not mounting another vehicle
            if np.setdiff1d([0, vehicle['name']], self.grid[new_row:new_row+vehicle[2], col]['name']).size != 0:
                return False
            # Set the old vehicle location as empty
            self.grid[row:row+vehicle[2], col] = (0, '', 0)
            # Move the vehicle to the new location
            self.grid[new_row:new_row+vehicle[2], col] = vehicle

        # Safe move in output file https://stackoverflow.com/questions/3345336/save-results-to-csv-file-with-python
        np.savetxt('output.csv', (vehicle[0], delta), delimiter=',')
        return True

    def __str__(self):
        return str(self.grid)


def setupgrid(game: int):
    if game == 1:
        vehicles = load_vehicles("Rushhour6x6_1.csv")
        grid = Grid(6)
        for vehicle in vehicles:
            grid.add_vehicle(vehicle)
        return grid

    elif game == 2:
        vehicles = load_vehicles("Rushhour6x6_2.csv")
        grid = Grid(6)
        for vehicle in vehicles:
            grid.add_vehicle(vehicle)
        return grid

    elif game == 3:
        vehicles = load_vehicles("Rushhour6x6_3.csv")
        grid = Grid(6)
        for vehicle in vehicles:
            grid.add_vehicle(vehicle)
        return grid

    elif game == 4:
        vehicles = load_vehicles("Rushhour9x9_4.csv")
        grid = Grid(9)
        for vehicle in vehicles:
            grid.add_vehicle(vehicle)
        return grid

    elif game == 5:
        vehicles = load_vehicles("Rushhour9x9_5.csv")
        grid = Grid(9)
        for vehicle in vehicles:
            grid.add_vehicle(vehicle)
        return grid

    elif game == 6:
        vehicles = load_vehicles("Rushhour9x9_6.csv")
        grid = Grid(9)
        for vehicle in vehicles:
            grid.add_vehicle(vehicle)
        return grid

    elif game == 7:
        vehicles = load_vehicles("Rushhour12x12_7.csv")
        grid = Grid(12)
        for vehicle in vehicles:
            grid.add_vehicle(vehicle)
        return grid
