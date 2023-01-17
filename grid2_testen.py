from Code.Classes.grid2 import *

if __name__ == "__main__":
    grid = setupgrid(1)
    print(grid)

    print(grid.move_possible(0,1,-1))
    if grid.move_possible(0,1,-1):
        grid.move_vehicle(0,1,-1)
        grid.update_grid()

    print(grid.grid)
    print(grid.move_possible(1,1,-1))
    if grid.move_possible(1,1,-1):
        grid.move_vehicle(1,1,-1)
        grid.update_grid()

    print(grid.grid)
