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

    def move_vehicle(self, vehicle):
        # If vehicle is horizontal
        if vehicle.orientation == 'H':
            # Move vehicle left (if coordinate is not 1) or right (if vehicle is not on the grid edge) 

            # Safe move in output file https://stackoverflow.com/questions/3345336/save-results-to-csv-file-with-python
            np.savetxt('output.csv', (car, move), delimiter=',')

        # If vehicle is vertical
        if vehicle.orientation == 'V':
            # Move vehicle up (if coordinate is not 1) or down (if vehicle is not on the grid edge)
            
            # Safe move in output file
            np.savetxt('output.csv', (car, move), delimiter=',')

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
