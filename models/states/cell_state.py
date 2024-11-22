import random


class CellState:
    def is_alive(self):
        raise NotImplementedError()

    def next_state(self, neighbors):
        raise NotImplementedError()

    def get_color(self):
        raise NotImplementedError()


class AliveState(CellState):
    def is_alive(self):
        return True

    def next_state(self, neighbors):
        alive_neighbors = len([n for n in neighbors if n.is_alive()])

        if alive_neighbors > 6:
            return InfectedState(0)
        elif alive_neighbors < 2 or alive_neighbors > 3:
            return DeadState()
        return self

    def get_color(self):
        return 'black'


class DeadState(CellState):
    def is_alive(self):
        return False

    def next_state(self, neighbors):
        alive_neighbors = len([n for n in neighbors if n.is_alive()])
        if alive_neighbors == 3:
            return AliveState()
        return self

    def get_color(self):
        return 'white'


class InfectedState(CellState):
    ttl = 4
    contagious_factor = 0.1

    def __init__(self, counter):
        self.counter = counter

    def is_alive(self):
        return True

    def next_state(self, neighbors):
        if self.counter > self.ttl*(1-self.contagious_factor):
            for n in neighbors:
                if n.is_alive():
                    n.set_state(self)
            return DeadState()

        if self.counter >= self.ttl:
            return DeadState()

        self.counter += 1
        return self

    def get_color(self):
        return 'yellow'
