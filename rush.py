from vehicle import *
from visualgrid import *
from grid import Grid, setupgrid
import csv

class RushHourGame:

    def __init__(self):
        pass





if __name__ == "__main__":
    filename = int(input("What game do you want to see/solve (1-7)?: "))
    grid = setupgrid(filename)
    visualize_grid(grid.grid, grid.dim)
