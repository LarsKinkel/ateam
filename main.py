from Code.Classes.vehicle import *
# from visualgrid import *
from Code.Algorithms.BFS import *
from Code.Algorithms.DFS import *
from Code.Algorithms.BFS_Heuristics import *
from helpers import *

import matplotlib.pyplot as plt
import csv
import os


if __name__ == "__main__":

    with open("output.csv", 'w') as file:
            dw = csv.DictWriter(file, delimiter=',', fieldnames= ["car", "move"])
            dw.writeheader()

    grid = setupgrid(4)
    visualize_grid(grid.grid, grid.dim)



    # --------------------------- Random Algorithm --------------------------
    # # Random algorithm that solves the rush hour game,
    #
    # # Create empty list to store random solutions
    # all_random_solutions = []
    # count_rsolutions = 0
    #
    # # Keep running the algorithm until ... solutions are found
    # while count_rsolutions < 100:
    #     # when starting and after finding solution, setup the initial state of the game
    #     grid = setupgrid(1)
    #     vehicles = grid.vehicles
    #
    #     # Solve game according to random algorithm
    #     Algorithm = Randomalgorithm(grid, vehicles)
    #
    #     # Append the amount of moves to the solutions list
    #     solution = Algorithm.solve()
    #     total_moves = solution[0]
    #     moves = solution[1]
    #     all_random_solutions.append((total_moves, moves))
    #     count_rsolutions += 1
    #     print(f"We now have {count_rsolutions} solutions")
    #
    # # Printing results
    # print("The solutions that are found are after:")
    # for solution in all_random_solutions:
    #     print(f"{solution[0]} moves, ")
    #
    # print()
    # print("Played game ...")
    # print()
    # print(f"The best solution after running the random algorithm {count_rsolutions} times is:")
    # print()
    # best_solution = min(all_random_solutions)
    # print(f"{best_solution[0]} moves until best solution.")
    #
    # worst_solution = max(all_random_solutions)
    # print(f"{worst_solution[0]} moves until worst solution")
    # print()
    # # write_to_output(best_solution[1])
    # hist = []
    # for solution in all_random_solutions:
    #     hist.append(solution[0])
    #
    # plt.title("Game ...: ... Random solutions ")
    # plt.ylabel("Frequency")
    # plt.xlabel("Moves made")
    # plt.xlim(right = 200000)
    # plt.hist(hist, bins = 50)
    # plt.show()
    #
    # visual(grid.visual, grid.dim, saveplot = True)

    # ---------------------------- BFS algorithm -------------------------------
    # # choose grid that you want to solve:
    # grid = setupgrid(1)
    #
    # # solving algorithm
    # algo = BFSalgorithm(grid)
    # algo.solve()

    # ---------------------------- DFS algorithm -------------------------------
    # # choose grid that you want to solve:
    # grid = setupgrid(1)
    #
    # # solving algorithm
    # algo = DFSalgorithm(grid)
    # algo.solve()

    # ------------------------- BFS 1st heuristic ------------------------------
    # # BFS with first heuristic (distance red car to final state)
    # grid = setupgrid(1)
    #
    # # solving algorithm
    # algo = BFS_H_algorithm(grid, 1)
    # algo.solve()

    # ------------------------- BFS 2nd heuristic ------------------------------
    # BFS with second heuristic (amount of blocking cars)
    # grid = setupgrid(3)
    # # BFS with second heuristic (amount of blocking cars)
    # grid = setupgrid(1)
    #
    # #
    # # solving algorithm
    # algo = BFS_H_algorithm(grid, 2)
    # algo.solve()
    #

    # ------------------------- BFS 3rd heuristic ------------------------------
    # BFS with third heuristic (manhattan distance)
    grid = setupgrid(1)
    goalstate = get_goal_state(copy.deepcopy(grid))
    
    # solving algorithm
    algo = BFS_H_algorithm(grid, 3, goalstate)
    algo.solve()
