from Code.Classes.vehicle import *
from visualgrid import *
from Code.Classes.grid2 import *
from Code.Algorithms.randomise import *
import matplotlib.pyplot as plt
import csv
import os


def get_manhattan_distance(vehicle, goal_position):
    """
    Pre: input a vehicle and its goal position
    Post: returns the manhattan distance of the vehicle towards his goal state
    """

    for vehicle_goal in goal_position.vehicles:
        if vehicle_goal.name == vehicle.name:
            xdist = abs(vehicle_goal.col - vehicle.col)
            ydist = abs(vehicle_goal.row - vehicle.row)

            ManDist = xdist + ydist

            return ManDist

# Heuristic 1: Distance red car to exit
def heuristics(grid , type, goalstate = None):

    # Heuristic 1: Distance red car to exit
    if type == 1:
        heuristic = 0

        # find column red car
        for vehicle in grid.vehicles:
            if vehicle.name == 99:
                redcar_col = vehicle.col
                break

        # determine final column depending on gridsize
        final_col = grid.dim - 1

        # add the distance of the redcar to the final column to the heuristic
        heuristic += final_col - redcar_col

        return heuristic

    # Heuristic 2: Nr of cars blocking the exit way of the red car
    elif type == 2:
        heuristic = 0

        # find row and col of red car
        for vehicle in grid.vehicles:
            if vehicle.name == 99:
                redcar_row = vehicle.row
                redcar_col = vehicle.col
                break

        for i in range(redcar_col + 1, grid.dim):
            if grid.grid[redcar_row - 1][i] != 0:
                heuristic += 1


        return heuristic

    # Heuristic 3: Manhattan Distance to goal
    elif type == 3:
        heuristic = 0

        for vehicle in grid.vehicles:
            ManDist = get_manhattan_distance(vehicle, goalstate)
            heuristic += ManDist

        return heuristic
