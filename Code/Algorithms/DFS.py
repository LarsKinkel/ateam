import copy
import sys
from .BFS import BFSalgorithm
sys.path.append("/Code/Classes")
from Code.Classes.grid2 import *
import queue
import numpy as np
import time

class DFSalgorithm(BFSalgorithm):

    def get_next_state(self):
        return self.states.pop()
