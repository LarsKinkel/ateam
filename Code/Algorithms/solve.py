import random
import sys
sys.path.append("/Code/Classes")
from Code.Classes.grid2 import *


# Random Algorithm
class Randomalgorithm:
    def __init__(self, grid, vehicles):
        self.vehicles = vehicles
        self.grid = grid


    def solve(self):
        grid = self.grid

        # Find red car
        for vehicle in self.vehicles:
            if vehicle.name == 99:
                redcar = vehicle
                print(redcar)

        count = 1
        # Move random cars untill coordinates of red car is 2,4
        while redcar.col != 5:

            random_vehicle = random.choice(self.vehicles)

            list = [-1, 1]
            random_delta = random.choice(list)

            try:
                if grid.move_possible(random_vehicle.row - 1, random_vehicle.col - 1, random_delta):

                    grid.move_vehicle(random_vehicle.row - 1, random_vehicle.col - 1, random_delta)
                    grid.update_grid()
                    # print(grid)
            except:
                print(random_vehicle.row - 1, random_vehicle.col - 1, random_delta)
                1/0
            count += 1
            if count == 1000:
                print("nu bij duizend")

        print(count)
        print(redcar)
