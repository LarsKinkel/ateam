from Code.Classes.grid2 import *
from Code.Algorithms.solve import *

if __name__ == "__main__":
    # grid = setupgrid(3)
    # print(grid)
    #
    # print(grid.move_possible(4,4,-1))
    # if grid.move_possible(4,4,-1):
    #     grid.move_vehicle(4,4,-1)
    #     grid.update_grid()
    #
    # print(grid.grid)
    #
    # print(grid.move_possible(2,5,1))
    # if grid.move_possible(3,5,-1):
    #     grid.move_vehicle(3,5,-1)
    #     grid.update_grid()

    grid = setupgrid(1)
    vehicles = grid.vehicles

    Algorithm = Randomalgorithm(grid, vehicles)
    Algorithm.solve()
