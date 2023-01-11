class Vehicle:
    """
    Vehicle object in the rush hour game, size can be 2x1 or 3x1

    Attributes:
        type: ?
        orientation: if the car is placed horizontally (H) or vertically (V)
        column: the column where the front of the car is placed
        row: the row where the the front of the car is placed
    """

    def __init__(self, name: str, orientation: str, col: int, row: int, length: int):
        self.name = name
        self.orientation = orientation
        self.col = col
        self.row = row
        self.length = length


def load_vehicles(filename: str):
    with open(filename, 'r') as file:
        header = file.readline().split(',')
        header[-1] = header[-1].strip()

        vehicles = []
        for line in file:
            splits = line.split(',')
            splits[-1] = splits[-1].strip()

            vehicle = Vehicle(splits[0], splits[1],
                              splits[2], splits[3], splits[4])
            vehicles.append(vehicle)

    return vehicles

# toevoegen dat een vehicle een bepaalde coordinaat heeft
# (bij horizontale voertuigen het linker blokje en bij verticale
# voertuigen de bovenste)
