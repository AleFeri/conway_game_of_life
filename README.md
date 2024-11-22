# Conway's Game of Life
###### *This project is still under developing*

This project is an interactive implementation of Conway's Game of Life, a cellular automaton devised by John Conway. The simulation features an interactive grid where cells evolve through generations based on simple rules, giving rise to complex and fascinating behaviors.

## Features

- Interactive PyQt-based UI for real-time simulation.
- Multiple initialization modes, including random states and predefined patterns.
- Adjustable simulation speed and custom cell manipulation.
- Modular design with a focus on clean code and extensibility.
- Clear separation of concerns leveraging design patterns.

---

## Design Choices

### Libraries
- **PyQt**: For building an interactive and responsive GUI.
- **Python's Standard Library**: For core logic and utilities.
- **Random Module**: For generating randomized initial states.

### Design Patterns
1. **State Pattern**:
   - Used for cell state management, encapsulating the logic for alive, dead, or other custom states (e.g., aging cells).
   - Ensures the behavior of cells is modular and extendable.

2. **Observer Pattern**:
   - Enables the grid to notify the UI of changes, ensuring synchronization between logic and visualization.

---

## Getting Started

### Prerequisites
Ensure Python 3.8+ is installed on your system.

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/AleFeri/conway_game_of_life.git
   cd conway-game-of-life
   ```
2.	Run the setup script to install dependencies and set up the environment:
   ```bash
   ./setup.sh
   ```
3. Launch the application:
   ```bash
   python main.py
   ```

### Requirements
The required libraries are listed in the requirements.txt file. They can be installed using:
   ```bash
   pip install -r requirements.txt
   ```
