import numpy as np
from vehicle import *

class Grid:
    """
    Grid object that states the size of the board.

    Attributes:
        vehicles: vehicles that are on the grid
        dimension: dimesion of the board
    """
    def __init__(self, dimension):
        self.grid = np.zeros((dimension, dimension))

    #Misschien moeten deze methods (add vehicle, move) in de Rush Hour class, want daar programmeren wij het echte spel

    def add_vehicle(self, vehicle):
        if vehicle.orientation == 'H':
            self.grid[vehicle.row - 1][vehicle.col - 1: vehicle.col - 1 + vehicle.length] = vehicle.name
        elif vehicle.orientation == 'V':
            self.grid[vehicle.row - 1: vehicle.row - 1 + vehicle.length, vehicle.col - 1] = vehicle.name

    def move_vehicle_forward(self, vehicle):
        # check of het horizontaal of verticaal moet
        # check wat de coordinaten zijn
        # schijf 1 hokje naar links of naar rechts
        pass

    def move_vehicle_backwards(self, vehicle):
        # check of het horizontaal of verticaal moet
        # check wat de coordinaten zijn
        # schijf 1 hokje naar links of naar rechts
        pass

    def __str__(self):
        return str(self.grid)


def setupgrid(game: int):
    if game == 1:
        vehicles = load_vehicles("Rushhour6x6_1.csv")
        grid = Grid(6)
        for vehicle in vehicles:
            grid.add_vehicle(vehicle)
        print(grid)

    elif game == 2:
        vehicles = load_vehicles("Rushhour6x6_2.csv")
        grid = Grid(6)
        for vehicle in vehicles:
            grid.add_vehicle(vehicle)
        print(grid)

    elif game == 3:
        vehicles = load_vehicles("Rushhour6x6_3.csv")
        grid = Grid(6)
        for vehicle in vehicles:
            grid.add_vehicle(vehicle)
        print(grid)

    elif game == 4:
        vehicles = load_vehicles("Rushhour9x9_4.csv")
        grid = Grid(9)
        for vehicle in vehicles:
            grid.add_vehicle(vehicle)
        print(grid)

    elif game == 5:
        vehicles = load_vehicles("Rushhour9x9_5.csv")
        grid = Grid(9)
        for vehicle in vehicles:
            grid.add_vehicle(vehicle)
        print(grid)

    elif game == 6:
        vehicles = load_vehicles("Rushhour9x9_6.csv")
        grid = Grid(9)
        for vehicle in vehicles:
            grid.add_vehicle(vehicle)
        print(grid)

    elif game == 7:
        vehicles = load_vehicles("Rushhour12x12_7.csv")
        grid = Grid(12)
        for vehicle in vehicles:
            grid.add_vehicle(vehicle)
        print(grid)
