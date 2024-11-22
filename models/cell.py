from PyQt5.QtGui import QBrush, QColor
from PyQt5.QtWidgets import QGraphicsRectItem
from models.states.cell_state import DeadState


class Cell:
    def __init__(self, row, col, size):
        self.next_generation_state = None
        self.row = row
        self.col = col
        self.size = size
        self.state = DeadState()

        self.graphics_item = QGraphicsRectItem(col * size, row * size, size, size)
        self.update_graphics()
        self.graphics_item.setPen(QColor("lightgray"))

    def set_state(self, state):
        self.state = state
        self.update_graphics()

    def is_alive(self):
        return self.state.is_alive()

    def calculate_next_state(self, neighbors):
        self.next_generation_state = self.state.next_state(neighbors)

    def next_state(self, neighbors):
        self.set_state(self.next_generation_state or self.state.next_state(neighbors))
        self.next_generation_state = None

    def update_graphics(self):
        self.graphics_item.setBrush(QBrush(QColor(self.state.get_color())))
