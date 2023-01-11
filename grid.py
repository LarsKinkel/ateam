class Grid:
    """
    Grid object that states the size of the board.

    Attributes:
        car: number of cars on the play board
        truck: number of trucks on the play board
        size: size of the board
    """
    def __init__(self, width, height, cars, trucks):
        self.width = width
        self.height = height
        self.cars = cars
        self.trucks = trucks
