import time
import numpy as np
from helpers import heuristics
import copy


class BFS_H_algorithm:
    def __init__(self, grid, heuristic_type, goalstate=None):
        self.vehicles = grid.vehicles
        self.grid = copy.deepcopy(grid)
        self.states = [(self.grid, [])]
        self.seen_states = []
        self.heuristic_type = heuristic_type
        self.iterations = 0

        self.goalstate = goalstate

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

        # Loop through all vehicles and their possible moves
        for vehicle in BFSgrid.vehicles:
            for delta in possible_moves:
                BFSgrid = copy.deepcopy(startstate)

                try:
                    if BFSgrid.move_possible(vehicle.row - 1, vehicle.col - 1, delta):
                        # startstate = copy.deepcopy(BFSgrid)
                        BFSgrid.move_vehicle(
                            vehicle.row - 1, vehicle.col - 1, delta)
                        # BFSgrid.store_move(vehicle.row - 1, vehicle.col - 1, delta)
                        BFSgrid.update_grid()

                        next_states.append((BFSgrid, (vehicle.name, delta)))

                except:
                    pass

        return next_states

    def seen(self, grid):
        for seen_state in self.seen_states:
            if np.array_equal(grid.grid, seen_state.grid):
                return True

        return False

    def solve(self):

        starttime = time.time()
        while self.states:
            state, moves = self.get_next_state()

            # calculate heuristic
            state.heuristic_score = heuristics(state, self.heuristic_type, self.goalstate)

            print(f'State depth: {state.depth}')
            # print(state)

            self.iterations += 1

            if state.is_solved():
                endtime = time.time()
                timerun = endtime - starttime
                print()
                print(f"Using BFS with Heuristic type {self.heuristic_type}:")
                print()
                print(f"Found a solution in {timerun} seconds: ")
                print(state)
                print()
                print("The path to the solution is:")
                print(moves)
                print()
                print(f"The ammount of moves is: {len(moves)}")
                print()
                print(f"Iterations: {self.iterations}")
                return moves
                break

            elif self.seen(state):
                continue

            # if a state is not yet in the seen states, append it to seen_states.
            self.seen_states.append(state)

            for next_state, move in self.get_next_states(state):
                next_state.depth = state.depth + 1
                next_state.heuristic_score = heuristics(next_state, self.heuristic_type, self.goalstate)
                self.states.append((next_state, moves + [move]))

            self.states = sorted(self.states, key=lambda x: x[0].heuristic_score)
