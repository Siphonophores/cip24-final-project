# Code In Place 2024 | Final Project
This is Sergio Barreto's final project submission.

# Conway's Game of Life
This is a simple implementation of [Conway's Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life) in Python.

## Requirements

- Python 3
- numpy

## Usage

1. Clone the repository:

```bash
git clone https://github.com/Siphonophores/cip24-final-project.git
cd cip24-final-project
```

2. Run the script:
```
python life.py
```

The script will display an animation of the Game of Life in your terminal. 
The animation will continue indefinitely until you stop it by pressing Ctrl+C.
Alternatively, you can uncomment:
```
# VERSION run for a fixed number of steps
    # for i in range(steps):
    #     display_grid(grid)
    #     grid = update_grid(grid)
    #     time.sleep(0.02)  # frame rate
```
and comment 
```
 try:
        while True:
            display_grid(grid)
            grid = update_grid(grid)
            time.sleep(0.02)  # frame rate
    except KeyboardInterrupt:
        print("\nYep")
```
to display the animation for a fixed number of steps.

## How it works

The script uses a 2D numpy array to represent the Game of Life grid. Each cell in the grid is either alive (represented by 1) or dead (represented by 0).

The initialize_grid function creates a random initial state for the grid.

The display_grid function displays the current state of the grid in the terminal.

The update_grid function calculates the next state of the grid based on the current state.

The run_simulation function runs the Game of Life simulation. It repeatedly updates the grid and displays the new state.

You can change the grid size to your liking by modifying the
```
# Parameters
width = 100
height = 60
steps = 500  # Number of steps to run the simulation
```
