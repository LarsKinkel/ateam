import copy
import sys
sys.path.append("/Code/Classes")
from Code.Classes.grid2 import *
from test_BFS import *
from queue import Queue

class BFSalgorithm:
    def __init__(self, grid):
        self.grid = copy.deepcopy(grid)
        self.vehicles = self.grid.vehicles



    def solve(self):

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

        # depth = ...                         # no deeper than 'depth'
        queue = Queue()
        seen_states = set()
        queue.put(self.grid)                       # add begin state to queue
        while not queue.empty():
            state = queue.get()              # get first from queue
            print(state)
            if redcar.col == solve_col:      # stop condition
                print("FOUNd")
                print(self.grid)
                break

            for next_state in find_all_next_states(state):
                if next_state not in seen_states:
                    seen_states.add(next_state)
                    queue.put(next_state)
                    self.grid = copy.deepcopy(next_state)
                    # print(self.grid)




                # for i in ['L', 'R']:            # for each possible action:
                #     child = copy.deepcopy(state)    # deepcopy the state
                #     child += i                      # make new child
                #     queue.put(child)                # add new child
