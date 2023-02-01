from Code.Classes.vehicle import *
from visualgrid import *
from Code.Classes.grid2 import *
from Code.Algorithms.randomise import *
from Code.Algorithms.BFS import *
from Code.Algorithms.DFS import *
from Code.Algorithms.BFS_Heuristics import *
from heuristics import *

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
            if move[0] > 26:
                if move[0] == 99:
                    namecar = chr(88)
                else:
                    namecar = "A" + chr(int(move[0]) - 26 + 64)
            else:
                namecar = chr(int(move[0]) + 64)

            writer.writerow((namecar, move[1]))

    print("The moves has been written to 'output.csv'")


def solution_visual(start_grid, moves, filename):
    for move in moves:
        for vehicle in start_grid.vehicles:
            if vehicle.name == move[0]:
                start_grid.move_vehicle(vehicle.row - 1, vehicle.col - 1, move[1])
                start_grid.update_grid()

    visual(start_grid.visual, start_grid.dim, saveplot = True, filename = filename)


def get_goal_state(grid):
    vehicles = grid.vehicles
    Algorithm = Randomalgorithm(grid, vehicles)
    goalstate = Algorithm.solve()[2]
    return goalstate

if __name__ == "__main__":

    # with open("output.csv", 'w') as file:
    #         dw = csv.DictWriter(file, delimiter=',', fieldnames= ["car", "move"])
    #         dw.writeheader()

    # grid = setupgrid(6)
    # visualize_grid(grid.grid, grid.dim)



    # --------------------------- Random reassignment --------------------------
    # # Random algorithm that solves the rush hour game,
    #
    # # Create empty list to store random solutions
    # all_random_solutions = []
    # count_rsolutions = 0
    #
    # # Keep running the algorithm until ... solutions are found
    # while count_rsolutions < 100:
    #     # when starting and after finding solution, setup the initial state of the game
    #     grid = setupgrid(7)
    #     vehicles = grid.vehicles
    #
    #     # Solve game according to random algorithm
    #     Algorithm = Randomalgorithm(grid, vehicles)
    #
    #     # Append the amount of moves to the solutions list
    #     total_moves, moves = Algorithm.solve()
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
    # print("Played game 7")
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
    # plt.title("Game 7: 100 Random solutions ")
    # plt.ylabel("Frequency")
    # plt.xlabel("Moves made")
    # plt.xlim(right = 200000)
    # plt.hist(hist, bins = 50)
    # plt.show()

    # visualize(grid.visual, grid.dim, saveplot = True)

    # ---------------------------- BFS algorithm -------------------------------
    # # choose grid that you want to solve:
    # grid = setupgrid(3)
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
    # BFS with first heuristic (distance red car to final state)
    grid = setupgrid(4)
    
    # solving algorithm
    algo = BFS_H_algorithm(grid, 1)
    algo.solve()

    # ------------------------- BFS 2nd heuristic ------------------------------
    # # BFS with second heuristic (amount of blocking cars)
    # grid = setupgrid(1)
    #
    # # solving algorithm
    # algo = BFS_H_algorithm(grid, 2)
    # algo.solve()


    # ------------------------- BFS 3th heuristic ------------------------------
    # # BFS with fifth heuristic (manhattan distance)
    # grid = setupgrid(7)
    # goalstate = get_goal_state(copy.deepcopy(grid))
    #
    # # solving algorithm
    # algo = BFS_H_algorithm(grid, 3, goalstate)
    # algo.solve()

    # moves = [(5, -1), (1, 1), (1, 1), (10, -1), (10, -1), (5, -1), (20, 1), (20, 1), (17, -1), (5, 1), (10, 1), (11, 1), (11, 1), (11, 1), (10, -1), (5, -1), (11, 1), (11, 1), (19, 1), (19, 1), (17, -1), (5, 1), (10, 1), (10, 1), (20, 1), (20, 1), (20, 1), (10, -1), (10, -1), (20, 1), (1, -1), (11, -1), (1, -1), (5,
    # 1), (7, -1), (7, -1), (7, -1), (5, -1), (1, 1), (1, 1), (5, -1), (11, 1), (12, -1), (21, -1), (21, -1), (12, -1), (13, -1), (22, 1), (22, 1), (18, -1), (18, -1), (22, 1), (13, 1), (12, 1), (12, 1), (18, -1), (14, -1), (14, -1), (21, 1), (21, 1), (22, 1), (5, -1), (6, -1), (2, -1), (1, 1), (6, -1), (22, 1), (22, 1), (1, -1), (1, -1), (22, 1), (6, 1), (2, 1), (6, 1), (5, 1), (99, -1), (99, -1), (8, -1), (3, -1), (8, -1), (9, -1), (9, -1), (9, -1), (3, -1),
    # (4, -1), (16, 1), (15, 1), (8, -1), (3, -1), (6, 1), (6, 1), (2, -1), (8, -1), (3, -1), (8, -1), (3, -1), (16, 1), (16, 1), (16, 1), (99, 1), (99, 1), (99, 1)]
    #
    # solution_visual(setupgrid(5), moves, "Game5_solution")
