import copy
import sys
sys.path.append("/Code/Classes")
from Code.Classes.grid2 import *
from test_BFS import *
import queue
import numpy as np
from collections import deque


class BFSalgorithm:
    def __init__(self, grid):
        self.vehicles = grid.vehicles
        self.grid = copy.deepcopy(grid)
        self.states = deque()
        self.seen_states = {}
        self.seen_states[copy.deepcopy(grid)] = 0
        self.count = 0

        self.states.appendleft(copy.deepcopy(grid))


    def get_next_state(self):
        return self.states.pop(0)


    def get_next_states(self, BFSgrid):
        """
        Pre: give function a grid object
        Post: Returnes a list of grid objects of that are possible next grids
              from the beginning grid.
        """

        possible_moves = [-1, 1]
        startstate = copy.deepcopy(BFSgrid)
        next_states = []

        # loop through all vehicles and their possible moves
        for vehicle in BFSgrid.vehicles:
            for delta in possible_moves:
                BFSgrid = copy.deepcopy(startstate)

                try:
                    if BFSgrid.move_possible(vehicle.row - 1, vehicle.col - 1, delta):
                        # startstate = copy.deepcopy(BFSgrid)
                        BFSgrid.move_vehicle(vehicle.row - 1, vehicle.col - 1, delta)
                        BFSgrid.update_grid()

                        next_states.append(BFSgrid)
                except:
                    pass

        return next_states

    def seen(self, grid):
        for seen_state in self.seen_states:
            if np.array_equal(grid.grid, seen_state.grid):
                return True

        return False


    def solve(self):

        while len(self.states) != 0:

            # get te next state from the list of states
            new_state = self.states.pop()
            self.count += 1

            # Find red car because we need to keep track of it's col to determine solution
            for vehicle in new_state.vehicles:
                if vehicle.name == 99:
                    redcar = vehicle

            if redcar.col > 0:
                print(redcar.col)

            # print("state:")
            # print(state.grid)

            if not new_state.is_solved():

                # if a the state is not yet in the seen states, append it to seen_states.
                # if len(self.seen_states) == 0:
                #     self.seen_states.append(state)
                # else:
                #     if not self.seen(state):
                #         self.seen_states.append(state)


                next_states = self.get_next_states(new_state)
                for next_state in next_states:
                    if next_state in self.seen_states:
                        pass
                    else:
                        self.states.appendleft(next_state)
                        self.seen_states[next_state] = new_state
            else:
                print()
                print(f"Found a solution: ")
                print(state)
                break
