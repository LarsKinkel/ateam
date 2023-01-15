from vehicle import *
from visualgrid import *
from grid import Grid, setupgrid
import csv


class RushHourGame:

    def __init__(self):
        pass


if __name__ == "__main__":
    # filename = int(input("What game do you want to see/solve (1-7)?: "))
    grid = setupgrid(1)
    visualize_grid(grid.grid, grid.dim)
    # Move vehicle at coordinates a given amount (depending on vehicle orientation)
    assert grid.move_vehicle(1, 0, -1) == True
    assert grid.move_vehicle(0, 2, -1) == False  # Border check
    assert grid.move_vehicle(1, 1, 1) == False  # Collission
    visualize_grid(grid.grid, grid.dim)
