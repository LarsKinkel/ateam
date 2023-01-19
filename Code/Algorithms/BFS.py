import queue, copy
import sys
sys.path.append("/Code/Classes")
from Code.Classes.grid2 import *

class BFSalgorithm:
    def __init__(self, grid, vehicles):
        self.vehicles = vehicles
        self.grid = grid


    def solve(self):
        grid = self.grid

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

            depth = ...                         # no deeper than 'depth'
            queue = queue.Queue()
            queue.put(grid)                       # add begin state to queue
            while not queue.empty():
                state = queue.get()              # get first from queue
                print(state)
                if redcar.col != solve_col:          # stop condition
                    for i in ['L', 'R']:            # for each possible action:
                        child = copy.deepcopy(state)    # deepcopy the state
                        child += i                      # make new child
                        queue.put(child)                # add new child
