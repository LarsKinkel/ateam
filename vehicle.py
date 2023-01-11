class Vehicle:
    """
    Vehicle object in the rush hour game, size can be 2x1 or 3x1

    Attributes:
        type: ?
        orientation: if the car is placed horizontally (0) or vertically (1)
        column: the column where the front of the car is placed
        row: the row where the the front of the car is placed
    """

    def __init__(self, type, orientation: int, col: int, row: int, length: int):
        self.type = type
        self.orientation = orientation
        self.col = col
        self.row = row
        self.length = length

# toevoegen dat een vehicle een bepaalde coordinaat heeft
# (bij horizontale voertuigen het linker blokje en bij verticale
# voertuigen de bovenste)
