

class Grid:
    """
    Grid object that states the size of the board.

    Attributes:
        car: number of cars on the play board
        truck: number of trucks on the play board
        size: size of the board
    """
    pass


class Car:
    """
    Car object in the rush hour game, size is 2x1

    Attributes:
        type: ?
        orientation: if the car is placed horizontally (0) or vertically (1)
        column: the column where the front of the car is placed
        row: the row where the the front of the car is placed
    """

    def __init__(self, type, orientation: int, col: int, row: int):
        pass


# Misschien is deze class overbodig?? Want alleen de size is verschillend. Dus het kan samen in de Car Class. Dus je hebt dan gewoon auto's met lengte 2 en lengte 3
class Truck:
    """
    Truck object in the rush hour game, size is 3x1

    Attributes:
        type: ?
        orientation: if the car is placed horizontally or vertically
        column: the column where the front of the car is placed
        row: the row where the the front of the car is placed
    """

    def __init__(self, type, orientation: int, col: int, row: int):
        pass

    # Deze load functie buiten de class definieren
    def load(filename: str):
        with open(filename, 'r') as file:
            header = file.readline().split(',')
            header[-1] = header[-1].strip()
            print(header)

            cars = []
            for line in file:
                splits = line.split(',')
                splits[-1] = splits[-1].strip()
                length = splits[4]

                if length == '2':
                    car = Car(splits[0], splits[1], splits[2], splits[3])
                elif length == '3':
                    truck = Truck(splits[0], splits[1], splits[2], splits[3])
                print(splits)


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
