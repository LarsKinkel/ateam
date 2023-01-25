import copy
import sys
sys.path.append("/Code/Classes")
from Code.Classes.grid2 import *
from test_BFS import *
import queue
import numpy as np

class BFS:
    def __init__(self, grid, vehicles):
        self.grid = copy.deepcopy(grid)
        self.vehicles = vehicles

        self.states = [copy.deepcopy(self.grid)]

        # self.best_solution = None
        # self.best_value = float('inf')

    def get_next_state(self):
        return self.states.pop(0)

    def build_children(self, grid):

    
