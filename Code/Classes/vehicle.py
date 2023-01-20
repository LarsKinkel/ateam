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

    def set_new_col(self, col):
        self.col = col

    def set_new_row(self, row):
        self.row = row

    def __repr__(self):
        return f'name: {self.name}, row: {self.row}, col: {self.col}'


def load_vehicles(filename: str):
    with open("gameboards/"+filename, 'r') as file:
        header = file.readline().split(',')
        header[-1] = header[-1].strip()

        vehicles = []
        for line in file:
            splits = line.split(',')
            splits[-1] = splits[-1].strip()

            if len(splits[0]) > 1:
                ascival = (ord(splits[0][0]) - 64) + (ord(splits[0][1]) - 37)
            elif len(splits[0]) == 1:
                ascival = ord(splits[0]) - 64
                if ascival == 24:
                    ascival = 99


            vehicle = Vehicle(ascival, splits[1], int(splits[2]), int(splits[3]), int(splits[4]))
            vehicles.append(vehicle)

    return vehicles

# toevoegen dat een vehicle een bepaalde coordinaat heeft
# (bij horizontale voertuigen het linker blokje en bij verticale
# voertuigen de bovenste)
