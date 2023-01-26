from Code.Classes.vehicle import *
from visualgrid import *
from Code.Classes.grid2 import *
from Code.Algorithms.randomise import *
from Code.Algorithms.BFS import *
import matplotlib.pyplot as plt
import csv, copy
import os

def find_all_next_states(BFSgrid):
    """ Function to find all next possible stages.

    Attributes:
    BFSgrid: start state
    """
    # Try to find all possible next states and store them in a list
    next_states = []
    vehicles = BFSgrid.vehicles
    possible_moves = [-1, 1]
    startstate = copy.deepcopy(BFSgrid)

    # Loop through all vehicles and their possible moves
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
                    print(next_states[0])
                    if not np.any(np.all(BFSgrid.grid == next_states)):
                        next_states.append(BFSgrid)

    return next_states


def get_next_states(BFSgrid):
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


def bfs_search(startgrid):
    queue = [startgrid]
    seen_states = []
    while queue:
        state = queue.pop(0)

        for vehicle in state.vehicles:
            if vehicle.name == 99:
                redcar = vehicle

        if redcar.col == 4:
            print("found solution")
            return True

        for next_state in get_next_states(state):
            if not np.any(np.all(next_state.grid == seen_states)):
                seen_states.append(next_state)
                queue.append(next_state)
        if redcar.col > 2:
            print(redcar.col)
            return True
    return False

if __name__ == '__main__':
    # Delete the existing CSV file:
    file = 'output.csv'
    if(os.path.exists(file) and os.path.isfile(file)):
        os.remove(file)

    # Print header of outputfile
    with open("output.csv", 'w') as file:
            dw = csv.DictWriter(file, delimiter=',', fieldnames= ["car", "move"])
            dw.writeheader()


    # --------------- check if BFS algorithm works as wanted -------------------

    # vehicles = load_vehicles("klein.csv")
    # grid = Grid(5, vehicles)
    grid = setupgrid(1)
    print(grid)
    algo = BFSalgorithm(grid)
    algo.solve()
    #
    # # check seen states list after ... iterations
    # for seen_state in algo.seen_states:
    #     print(seen_state.grid)
    #     print()

    # ------------- check if get_next_states function works as wanted ----------

    # print("State inserted is:")
    # print()
    # vehicles = load_vehicles("klein.csv")
    # grid = Grid(3, vehicles)
    # grid = setupgrid(1)
    # # bfs_search(grid)
    # print(grid)
    # # print(BFSgrid)
    # # print()
    #
    # print("All next states from state inserted are: ")
    # print()
    #
    # next_states = get_next_states(grid)
    # for state in next_states:
    #     print(state)
    #     print()
    #
    # print("pop next state: ")
    # print()
    # state0 = next_states.pop(0)
    # print(state0)
    # print()
    #
    # print("next states:")
    # print()
    # next_states = get_next_states(state0)
    # for state in next_states:
    #     print(state)
    #     print()
    #
    # print("pop next state: ")
    # print()
    # state1 = next_states.pop(0)
    # print(state1)
    # print()
    #
    # print("next states:")
    # print()
    # next_states = get_next_states(state1)
    # for state in next_states:
    #     print(state)
    #     print()
    #
    # print(f"Total of {len(next_states)} states are possible after last state")


    # ------------------ check if seen() function works as wanted --------------
    # grid = setupgrid(1)
    # algo = BFSalgorithm(grid)
    # algo.seen_states.append(grid)
    #
    # for seen_state in algo.seen_states:
    #     print(seen_state.grid)
    #
    # grid2 = setupgrid(1)
    # print(algo.seen(grid2))
