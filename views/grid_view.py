import random
from copy import copy

from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QGraphicsView, QGraphicsScene
from models.cell import Cell
from models.states.cell_state import AliveState


class GridView(QGraphicsView):
    def __init__(self, rows, cols, cell_size):
        super().__init__()
        self.grid = []
        self.scene = QGraphicsScene()
        self.setScene(self.scene)

        self.timer = QTimer()
        self.timer.timeout.connect(self.compute_generation)

        self.rows = rows
        self.cols = cols
        self.cell_size = cell_size

        self.create_grid()

    def create_grid(self):
        self.grid = []
        for row in range(self.rows):
            grid_row = []
            for col in range(self.cols):
                cell = Cell(row, col, self.cell_size)
                self.scene.addItem(cell.graphics_item)
                grid_row.append(cell)
            self.grid.append(grid_row)

        self.randomize_grid()

    def randomize_grid(self):
        if not self.grid:
            self.create_grid()

        for grid_row in self.grid:
            for cell in grid_row:
                if (
                    cell.row != 0 and
                    cell.col != 0 and
                    (cell.row % random.randint(1, self.rows) == 0 or cell.col % random.randint(1, self.cols) == 0)
                ):
                    cell.set_state(AliveState())

    def start_simulation(self, interval=1000):
        self.timer.start(interval)

    def stop_simulation(self):
        self.timer.stop()

    def compute_generation(self):
        for grid_row in self.grid:
            for cell in grid_row:
                cell.calculate_next_state(self.find_neighbors(cell))
        for grid_row in self.grid:
            for cell in grid_row:
                cell.next_state(self.find_neighbors(cell))

    def find_neighbors(self, cell):
        neighbors = []
        directions = [
            (-1, -1),
            (-1, 0), (-1, 1),
            (0, -1), (0, 1),
            (1, -1),
            (1, 0), (1, 1)
        ]

        for dr, dc in directions:
            neighbor_row = cell.row + dr
            neighbor_col = cell.col + dc

            neighbors.append(self.grid[neighbor_row % self.rows][neighbor_col % self.cols])

        return neighbors

    def reset(self):
        self.stop_simulation()
        self.create_grid()
