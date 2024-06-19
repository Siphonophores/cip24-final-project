import numpy as np
import time
import os

# receive p as an argument to initialize_grid to set the probability of a cell being alive
def initialize_grid(height, width, p=0.5):
    return np.random.choice([0, 1], size=(height, width), p=[1-p, p])

def display_grid(grid):
    os.system('clear') # clear the terminal for animation effect
    for row in grid:
        print(''.join(['⬜' if cell else '⬛' for cell in row]))
    print("\n")

def update_grid(grid):
    new_grid = grid.copy() 
    rows, cols = grid.shape # unpacking is like destructuring in JS

    for i in range(rows):
        for j in range(cols):
            # modulo to wrap around the edges, torus ftw
            # Naming each neighbor with indices for human

            # NO WRAP VERSION
            # top_left = grid[i-1, j-1] if i > 0 and j > 0 else 0
            # top = grid[i-1, j] if i > 0 else 0
            # top_right = grid[i-1, j+1] if i > 0 and j < cols-1 else 0
            # left = grid[i, j-1] if j > 0 else 0
            # right = grid[i, j+1] if j < cols-1 else 0
            # bottom_left = grid[i+1, j-1] if i < rows-1 and j > 0 else 0
            # bottom = grid[i+1, j] if i < rows-1 else 0
            # bottom_right = grid[i+1, j+1] if i < rows-1 and j < cols-1 else 0

            # WRAP VERSION
            top_left = grid[(i-1) % rows, (j-1) % cols]
            top = grid[(i-1) % rows, j]
            top_right = grid[(i-1) % rows, (j+1) % cols]
            left = grid[i, (j-1) % cols]
            right = grid[i, (j+1) % cols]
            bottom_left = grid[(i+1) % rows, (j-1) % cols]
            bottom = grid[(i+1) % rows, j]
            bottom_right = grid[(i+1) % rows, (j+1) % cols]

            # Sum of neighbors
            total = (top_left + top + top_right + 
                     left + right + 
                     bottom_left + bottom + bottom_right)

            # If cell is alive and has less than 2 or more than 3 neighbors, kaput
            if grid[i, j] == 1:
                if total < 2 or total > 3:
                    new_grid[i, j] = 0
            # If cell is dead and has exactly 3 neighbors, rise child
            else:
                if total == 3:
                    new_grid[i, j] = 1
    return new_grid

def reinitialize_patch(grid, height, width, patch_size=10, p=0.25):
    x, y = np.random.randint(0, height-patch_size), np.random.randint(0, width-patch_size) # Randomly select a patch
    grid[x:x+patch_size, y:y+patch_size] = initialize_grid(patch_size, patch_size, p=p)
    return grid

def run_simulation(height, width):
    grid = initialize_grid(height, width)
    try:
        step = 0
        while True:
            display_grid(grid)
            grid = update_grid(grid)
            if step % 50 == 0:
                grid = reinitialize_patch(grid, height, width)
            step += 1
            time.sleep(0.005)  # Pause to visualize changes
    except KeyboardInterrupt:
        print("Run steps:", step)

# Parameters
width = 100
height = 60
steps = 500  # Number of steps to run the simulation

run_simulation(height, width) # add steps as an argument to run_simulation to run for a fixed number of steps