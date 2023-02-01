from Code.Algorithms.randomise import *

def write_to_output(moves):
    # Keep track of the moves in the outputfile
    with open("output.csv", 'w+') as f:
        dw = csv.DictWriter(f, delimiter=',', fieldnames= ["car", "move"])
        dw.writeheader()
        writer = csv.writer(f)

        for move in moves:
            if move[0] > 26:
                if move[0] == 99:
                    namecar = chr(88)
                else:
                    namecar = "A" + chr(int(move[0]) - 26 + 64)
            else:
                namecar = chr(int(move[0]) + 64)

            writer.writerow((namecar, move[1]))

    print("The moves has been written to 'output.csv'")


def solution_visual(start_grid, moves, filename):
    for move in moves:
        for vehicle in start_grid.vehicles:
            if vehicle.name == move[0]:
                start_grid.move_vehicle(vehicle.row - 1, vehicle.col - 1, move[1])
                start_grid.update_grid()

    visual(start_grid.visual, start_grid.dim, saveplot = True, filename = filename)


def get_goal_state(grid):
    vehicles = grid.vehicles
    Algorithm = Randomalgorithm(grid, vehicles)
    goalstate = Algorithm.solve()[2]
    return goalstate


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
