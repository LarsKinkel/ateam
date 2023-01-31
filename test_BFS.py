from Code.Classes.vehicle import *
from visualgrid import *
from Code.Classes.grid2 import *
from Code.Algorithms.randomise import *
from Code.Algorithms.BFS import *
from Code.Algorithms.DFS import *
from main import *
import matplotlib.pyplot as plt
import csv, copy
import os


if __name__ == '__main__':
    # Delete the existing CSV file:
    # file = 'output.csv'
    # if(os.path.exists(file) and os.path.isfile(file)):
    #     os.remove(file)

    # Print header of outputfile



    # --------------- check if BFS algorithm works as wanted -------------------

    # vehicles = load_vehicles("klein.csv")
    # grid = Grid(5, vehicles)
    grid = setupgrid(3)
    print(grid)
    algo = BFSalgorithm(grid)
    moves = algo.solve()
    write_to_output(moves)
    solution_visual(grid, moves, "Game3_solution")
    #
    # # check seen states list after ... iterations
    # for seen_state in algo.seen_states:
    #     print(seen_state.grid)
    #     print()

    # --------------- check if DFS algorithm works as wanted -------------------

    # vehicles = load_vehicles("klein.csv")
    # grid = Grid(5, vehicles)
    # grid = setupgrid(3)
    # print(grid)
    # algo = DFSalgorithm(grid)
    # algo.solve()
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
