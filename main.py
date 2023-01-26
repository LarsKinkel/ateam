from Code.Classes.vehicle import *
from visualgrid import *
from Code.Classes.grid2 import *
from Code.Algorithms.randomise import *
import matplotlib.pyplot as plt
import csv
import os

if __name__ == "__main__":

    with open("output.csv", 'w') as file:
            dw = csv.DictWriter(file, delimiter=',', fieldnames= ["car", "move"])
            dw.writeheader()

    # grid = setupgrid(6)
    # visualize_grid(grid.grid, grid.dim)



    # --------------------------- Random Algorithm --------------------------
    # Random algorithm that solves the rush hour game,

    # create empty list to store random solutions
    all_random_solutions = []
    count_rsolutions = 0

    # keep running the algorithm until ... solutions are found
    while count_rsolutions < 10:
        # when starting and after finding solution, setup the initial state of the game
        grid = setupgrid(1)
        vehicles = grid.vehicles

        # solve game according to random algorithm
        Algorithm = Randomalgorithm(grid, vehicles)

        # append the amount of moves to the solutions list if under 80.000
        solution = Algorithm.solve()
        if solution < 80000:
            all_random_solutions.append(solution)
        count_rsolutions += 1
        print(count_rsolutions)
    # printing results
    print("The solutions that are found are after:")
    for solution in all_random_solutions:
        print(f"{solution} moves, ")

    print()
    print(f"The best solution after running the random algorithm {count_rsolutions} times is:")
    print()
    print(f"{min(all_random_solutions)} moves until solution.")
    print()
    plt.hist(all_random_solutions, bins = 100)
    plt.show()

    visualize(grid.visual, grid.dim, saveplot = True)

    # ---------------------------- BFS algorithm -------------------------------
    ## choose grid that you want to solve:
    # grid = setupgrid(1)
    # algo = BFSalgorithm(grid)
    # algo.solve()

    # ---------------------------- DFS algorithm -------------------------------
    ## choose grid that you want to solve:
    # grid = setupgrid(1)
    # algo = DFSalgorithm(grid)
    # algo.solve()
