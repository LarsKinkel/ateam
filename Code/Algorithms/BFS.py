import copy
import sys
sys.path.append("/Code/Classes")
from Code.Classes.grid2 import *
from test_BFS import *
import queue


class BFSalgorithm:
    def __init__(self, grid, vehicles):
        self.vehicles = vehicles
        self.grid = copy.deepcopy(grid)

        self.states = []
        self.states.append(copy.deepcopy(grid))


    def get_next_state(self):
        return self.states.pop(0)


    def get_next_states(self, BFSgrid):
        # try to find all possible next states and store them in a list

        vehicles = BFSgrid.vehicles
        possible_moves = [-1, 1]
        startstate = copy.deepcopy(BFSgrid)
        next_states = []

        # loop through all vehicles and their possible moves
        for vehicle in vehicles:
            for delta in possible_moves:
                BFSgrid = startstate
                if BFSgrid.move_possible(vehicle.row - 1, vehicle.col - 1, delta):
                    startstate = copy.deepcopy(BFSgrid)
                    BFSgrid.move_vehicle(vehicle.row - 1, vehicle.col - 1, delta)
                    BFSgrid.update_grid()

                    # if the state is not yet in the possible next states, append
                    if BFSgrid not in next_states:
                        next_states.append(BFSgrid)

        return next_states



    def solve(self):

        # Find red car
        for vehicle in self.vehicles:
            if vehicle.name == 99:
                redcar = vehicle
                # print(redcar)

        # Set goal column for the red car for the different dimensions
        if self.grid.dim == 6:
            solve_col = 5
        elif self.grid.dim == 9:
            solve_col = 8
        elif self.grid.dim == 12:
            solve_col = 11


        seen_states = set()
        i = 0
        while self.states:
            # print(i)
            i += 1
            state = self.get_next_state()        # get first from queue
            # print(len(self.states))

            # Find red car
            for vehicle in state.vehicles:
                if vehicle.name == 99:
                    redcar = vehicle

            if redcar.col > 1:
                print(redcar.col)

            if redcar.col != solve_col:
                for next_state in self.get_next_states(state):
                    if next_state not in seen_states:
                        seen_states.add(next_state)
                        self.states.append(next_state)

            else:
                print(f"Found a solution: {state}")
