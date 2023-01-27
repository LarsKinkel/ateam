from Code.Classes.vehicle import *
from visualgrid import *
from Code.Classes.grid2 import *
from Code.Algorithms.randomise import *
import matplotlib.pyplot as plt
import csv
import os

def write_to_output(moves):
    # Keep track of the moves in the outputfile
    with open("output.csv", 'w+') as f:
        dw = csv.DictWriter(f, delimiter=',', fieldnames= ["car", "move"])
        dw.writeheader()
        writer = csv.writer(f)

        for move in moves:
            if move[0] == 99:
                namecar = chr(int(24)+64)
            else:
                namecar = chr(int(move[0])+64)
            writer.writerow((namecar, move[1]))

    print("The moves has been written to 'output.csv'")

def solution_visual(start_grid, moves, filename):
    for move in moves:
        for vehicle in start_grid.vehicles:
            if vehicle.name == move[0]:
                start_grid.move_vehicle(vehicle.row - 1, vehicle.col - 1, move[1])
                start_grid.update_grid()

    visual(start_grid.visual, start_grid.dim, saveplot = True, filename = filename)




if __name__ == "__main__":

    # with open("output.csv", 'w') as file:
    #         dw = csv.DictWriter(file, delimiter=',', fieldnames= ["car", "move"])
    #         dw.writeheader()

    # grid = setupgrid(6)
    # visualize_grid(grid.grid, grid.dim)



    # --------------------------- Random reassignment --------------------------
    # Random algorithm that solves the rush hour game,

    # create empty list to store random solutions
    all_random_solutions = []
    count_rsolutions = 0

    # keep running the algorithm until ... solutions are found
    while count_rsolutions < 1:
        # when starting and after finding solution, setup the initial state of the game
        grid = setupgrid(1)
        vehicles = grid.vehicles

        # solve game according to random algorithm
        Algorithm = Randomalgorithm(grid, vehicles)

        # append the amount of moves to the solutions list
        total_moves, moves = Algorithm.solve()
        all_random_solutions.append((total_moves, moves))
        count_rsolutions += 1

    # printing results
    print("The solutions that are found are after:")
    for solution in all_random_solutions:
        print(f"{solution[0]} moves, ")

    print()
    print(f"The best solution after running the random algorithm {count_rsolutions} times is:")
    print()
    best_solution = min(all_random_solutions)
    print(f"{best_solution[0]} moves until solution.")
    print()
    write_to_output(best_solution[1])
    hist = []
    for solution in all_random_solutions:
        hist.append(solution[0])
    plt.hist(hist, bins = 50)
    plt.show()

    # visualize(grid.visual, grid.dim, saveplot = True)

    # --------------------------- BFS Algorithm --------------------------------
