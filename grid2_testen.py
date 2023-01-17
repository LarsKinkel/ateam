from Code.Classes.grid2 import *

if __name__ == "__main__":
    grid = setupgrid(1)
    print(grid)

    print(grid.move_possible(0,3,-1))
    if grid.move_possible(0,1,-1):
        new_grid = grid.update_grid()

    print(new_grid)
    print(grid.move_possible(1,1,-1))
    if grid.move_possible(1,1,-1):
        new_grid = grid.update_grid()

    print(new_grid)
