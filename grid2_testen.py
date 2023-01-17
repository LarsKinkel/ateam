from Code.Classes.grid2 import *

if __name__ == "__main__":
    grid = setupgrid(1)
    print(grid)

    grid.move_vehicle(4,4,-1)

    new_grid = grid.get_grid()
    print(new_grid)

    grid.move_vehicle(2,5, -1)

    new_grid = grid.get_grid()
    print(new_grid)
