from Code.Classes.vehicle import *
from visualgrid import *
from Code.Classes.grid2 import Grid, setupgrid
import csv


class RushHourGame:

    def __init__(self):
        pass


if __name__ == "__main__":
    # filename = int(input("What game do you want to see/solve (1-7)?: "))
    with open("output.csv", 'w') as file:
            dw = csv.DictWriter(file, delimiter=',', fieldnames= ["car", "move"])
            dw.writeheader()

    grid = setupgrid(1)
    
    grid.move_vehicle(0,1,-1)
    grid.update_grid()
    
    grid.move_vehicle(1, 1, -1)
    grid.update_grid()
    
    grid.move_vehicle(0, 3, -1)
    grid.update_grid()

    grid.move_vehicle(2,2,1)
    grid.update_grid()

    grid.move_vehicle(3,0,1)
    grid.update_grid()

    grid.move_vehicle(4,0,1)
    grid.update_grid()

    grid.move_vehicle(4,4,-1)
    grid.update_grid()

    grid.move_vehicle(2,5,-1)
    grid.update_grid()

    grid.move_vehicle(3,5,-1)
    grid.update_grid()

    grid.move_vehicle(3,3,1)
    grid.update_grid()

    grid.move_vehicle(1,3,-1)
    grid.update_grid()

    grid.move_vehicle(0,2,1)
    grid.update_grid()

    grid.move_vehicle(1,2,1)
    grid.update_grid()

    grid.move_vehicle(2,0,1)
    grid.update_grid()

    grid.move_vehicle(2,3,1)
    grid.update_grid()

    visualize(grid.visual, grid.dim, saveplot = True)

