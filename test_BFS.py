from Code.Classes.vehicle import *
from visualgrid import *
from Code.Classes.grid2 import *
from Code.Algorithms.randomise import *
from Code.Algorithms.BFS import *
import matplotlib.pyplot as plt
import csv, copy
import os

def find_all_next_states(BFSgrid):
    # try to find all possible next states and store them in a list
    next_states = []
    vehicles = BFSgrid.vehicles
    possible_moves = [-1, 1]
    startstate = copy.deepcopy(BFSgrid)

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

if __name__ == '__main__':

    # Delete the existing CSV file:
    # file = 'output.csv'
    # if(os.path.exists(file) and os.path.isfile(file)):
    #     os.remove(file)

    # Print header of outputfile
    # with open("output.csv", 'w') as file:
    #         dw = csv.DictWriter(file, delimiter=',', fieldnames= ["car", "move"])
    #         dw.writeheader()

    # print("State inserted is:")
    # print()
    BFSgrid = setupgrid(1)
    # print(BFSgrid)
    # BFSgrid.move_vehicle(0,1,-1)
    # BFSgrid.update_grid()
    # print(BFSgrid)
    # BFSgrid.move_vehicle(1,1,-1)
    # BFSgrid.update_grid()
    # print(BFSgrid)
    # BFSgrid.move_vehicle(2,2,1)
    # BFSgrid.update_grid()
    # print(BFSgrid)
    # BFSgrid.move_vehicle(2,2,1)
    # BFSgrid.update_grid()
    # print(BFSgrid)
    # print()
    # for i in find_all_next_states(BFSgrid):
    #     print(i)
    #
    # print()
    #
    # print("All next states from state inserted are: ")
    # print()
    #
    # next_states = find_all_next_states(BFSgrid)
    # for state in next_states:
    #     print(state)
    #     print()
    #
    # print(f"Total of {len(next_states)} states are possible after beginstate")

    algo = BFSalgorithm(BFSgrid)
    algo.solve()
