import copy
import sys
sys.path.append("/Code/Classes")
from Code.Classes.grid2 import *
from test_BFS import *
import queue
import numpy as np


class BFSalgorithm:
    def __init__(self, grid, vehicles):
        self.vehicles = vehicles
        self.grid = copy.deepcopy(grid)

        self.states = []
        self.states.append(copy.deepcopy(grid))


    def get_next_state(self):
        return self.states.pop(0)


    def get_next_states(self, BFSgrid):
        """
        Pre: give function a grid object
        Post: Returnes a list of grid objects of that are possible next grids
              from the beginning grid.
        """


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
                    if len(next_states) == 0:
                        next_states.append(BFSgrid)
                    else:
                        for next_state in next_states:
                            if not np.array_equal(BFSgrid.grid, next_state.grid):
                                next_states.append(BFSgrid)

        return next_states


    def solve(self):

        # Find red car
        # for vehicle in self.vehicles:
        #     if vehicle.name == 99:
        #         redcar = vehicle
                # print(redcar)

        # Set goal column for the red car for the different dimensions
        if self.grid.dim == 6:
            solve_col = 5
        elif self.grid.dim == 9:
            solve_col = 8
        elif self.grid.dim == 12:
            solve_col = 11

        # seen_states = []

        while self.states:
            # print(len(self.states))

            # get te next state from the list of states
            state = self.get_next_state()
            # print(f"states in stateslist: {len(self.states)}")
            # print()

            # Find red car because we need to keep track of it's col to determine solution
            for vehicle in state.vehicles:
                if vehicle.name == 99:
                    redcar = vehicle

            if redcar.col > 2:
                print(redcar.col)
                print()

            # print("state:")
            # print(state.grid)

            if redcar.col != solve_col:

                # if a the state is not yet in the seen states, append it to seen_states.
                # if len(seen_states) == 0:
                #     seen_states.append(state)

                # for seen_state in seen_states:
                #     if not np.array_equal(state.grid, seen_state.grid):
                #         seen_states.append(state)

                # print("seen states: ")
                # for seen_state in seen_states:
                    # print(seen_state)
                    # print()
                # print(len(seen_states))
                next_states = self.get_next_states(state)
                for next_state in next_states:
                    # print(f"next state: {next_state}")
                    # for seen_state in seen_states:
                    #     if not np.array_equal(next_state.grid, seen_state.grid):
                    self.states.append(next_state)
                            # seen_states.append(next_state)
            else:
                print()
                print(f"Found a solution: ")
                print(state)
                break
