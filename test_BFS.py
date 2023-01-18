from Code.Classes.vehicle import *
from visualgrid import *
from Code.Classes.grid2 import *
from Code.Algorithms.randomise import *
import matplotlib.pyplot as plt
import csv

def find_all_next_states(BFSgrid, game):
    # try to find all possible next states and store them in a list
    next_states = []
    vehicles = BFSgrid.vehicles
    pos_moves = [-1, 1]

    for vehicle in vehicles:
        for delta in pos_moves:
            BFSgrid = setupgrid(game)
            if BFSgrid.move_possible(vehicle.row - 1, vehicle.col - 1, delta):
                BFSgrid.move_vehicle(vehicle.row - 1, vehicle.col - 1, delta)
                BFSgrid.update_grid()
                if BFSgrid not in next_states:
                    next_states.append(BFSgrid)

    return next_states

if __name__ == '__main__':

    print("State inserted is:")
    print()
    BFSgrid = setupgrid(1)
    print(BFSgrid)
    print()

    print("All next states from state inserted are: ")
    print()

    next_states = find_all_next_states(BFSgrid, 1)
    for state in next_states:
        print(state)
        print()

    print(f"Total of {len(next_states)} states are possible after beginstate")
