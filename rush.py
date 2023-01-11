import csv

class Grid:
    """
    Grid object that states the size of the board.
    """
    def __init__(self, width, height, cars, trucks):
        self.width = width
        self.height = height
        self.cars = cars
        self.trucks = trucks


class Car:
    """
    Car object in the rush hour game, size is 2x1
    """
    def __init__(self, type, orientation, col, row):
        self.type = type
        self.orientation = orientation
        self.col = col
        self.row = row

    def places(self, orientation, col, row):
        if orientation = 'H':



class Truck:
    """
    Truck object in the rush hour game, size is 3x1
    """
    def __init__(self, type, orientation, col, row):
        self.type = type
        self.orientation = orientation
        self.col = col
        self.row = row

def load(filename: str):
    with open(filename, 'r') as file:
        header = file.readline().split(',')
        header[-1] = header[-1].strip()
        print(header)

        cars = []
        trucks = []
        for line in file:
            splits = line.split(',')
            splits[-1] = splits[-1].strip()
            length = splits[4]

            if length == '2':
                car = Car(splits[0], splits[1], splits[2], splits[3])
                cars.append(car)
            elif length == '3':
                truck = Truck(splits[0], splits[1], splits[2], splits[3])
                trucks.append(truck)

    print(len(cars))
    print(len(trucks))
    print(cars[1].type)


if __name__ == "__main__":
    load("Rushhour6x6_1.csv")


# def make_knapsack(filename: str) -> Knapsack:
#     with open(filename, 'r') as file:
#         header = file.readline()
#         for line in file:
#             splits = line.split(',')
#             if len(splits) > 3:
#                 element = splits[0].strip()
#                 points = int(splits[1])
#                 weight = int(splits[2])
#                 volume = int(splits[3])
#                 if element == 'knapsack':
#                     knapsack = Knapsack(Resources(weight, volume))
#     return knapsack
