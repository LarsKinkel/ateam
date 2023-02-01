from .BFS import BFSalgorithm


class DFSalgorithm(BFSalgorithm):

    def get_next_state(self):
        return self.states.pop()
