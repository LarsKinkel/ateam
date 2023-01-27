import random
import sys
sys.path.append("/Code/Classes")
from Code.Classes.grid2 import *

# Random Algorithm
class Randomalgorithm:
    """ A random algorith to solve the Rush Hour puzzle

        Attributes:
        grid: Grid object
        vehicles: List of vehicles that are in the grid
    """
    def __init__(self, grid, vehicles):
        self.vehicles = vehicles
        self.grid = grid

    def solve(self):
        grid = self.grid
        path = []

        # Find red car
        for vehicle in self.vehicles:
            if vehicle.name == 99:
                redcar = vehicle
                # print(redcar)
        total_moves = 0

        # Move random cars untill red car is in the right column for the different dimensions
        if self.grid.dim == 6:
            solve_col = 5
        elif self.grid.dim == 9:
            solve_col = 8
        elif self.grid.dim == 12:
            solve_col = 11

        while redcar.col != solve_col:

            random_vehicle = random.choice(self.vehicles)

            moves = [-1, 1]
            random_delta = random.choice(moves)

            try:
                if grid.move_possible(random_vehicle.row - 1, random_vehicle.col - 1, random_delta):

                    grid.move_vehicle(random_vehicle.row - 1, random_vehicle.col - 1, random_delta)
                    path.append((random_vehicle.name, random_delta))
                    grid.update_grid()
                    total_moves += 1
                    # print(grid)
            except:
                print(random_vehicle.row - 1, random_vehicle.col - 1, random_delta)



            # Print the number of iterations at every 10.000th iteration
            if total_moves % 10000 == 0:
                print(f"{total_moves} moves made")

        print(f'Solution found after {total_moves} moves. ')
        print("The grid looks as follows at solved state:")
        print(grid)
        return total_moves, path
