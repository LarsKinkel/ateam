import copy
import sys
sys.path.append("/Code/Classes")
from Code.Classes.grid2 import *
import queue
import numpy as np
import time

class Astar:
    def __init__(self, grid):
        self.openlist = [copy.deepcopy(grid)]
        self.closedlist = []

    def solve(self):

        while self.openlist:
            
