from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QPushButton, QGridLayout
from views.grid_view import GridView


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Game of Life")
        self.setGeometry(100, 100, 800, 600)

        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)

        self.grid_view = GridView(100, 100, 10)
        layout.addWidget(self.grid_view)
        self.setCentralWidget(central_widget)

        start_button = QPushButton("Start")
        start_button.clicked.connect(self.grid_view.start_simulation)

        stop_button = QPushButton("Stop")
        stop_button.clicked.connect(self.grid_view.stop_simulation)

        reset_button = QPushButton("Reset")
        reset_button.clicked.connect(self.grid_view.reset)

        action_row = QGridLayout()
        buttons = [start_button, stop_button, reset_button]
        for i, button in enumerate(buttons):
            action_row.addWidget(button, 0, i)

        layout.addLayout(action_row)