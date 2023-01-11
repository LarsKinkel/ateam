from vehicle import *
from grid import Grid
import csv

class RushHourGame:

    def __init__(self):
        pass





if __name__ == "__main__":
    vehicles = load_vehicles("Rushhour6x6_1.csv")
    grid = Grid(6)

    for vehicle in vehicles:
        grid.add_vehicle(vehicle)

    print(grid)
