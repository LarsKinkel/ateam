from Code.Classes.grid2 import *
from Code.Algorithms.randomise import *

if __name__ == "__main__":
    with open("output.csv", 'w') as file:
            dw = csv.DictWriter(file, delimiter=',', fieldnames= ["car", "move"])
            dw.writeheader()
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
    grid1 = setupgrid(2)
    print(grid == grid1)
    print(grid.grid.all() == grid1.grid.all())
    print(np.array_equal(grid.grid, grid1.grid))

    # vehicles = grid.vehicles

    # Algorithm = Randomalgorithm(grid, vehicles)
    # Algorithm.solve()
