# life-matplot.py

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
import matplotlib.animation as animation
import itertools
from matplotlib.widgets import Button

rcParams['toolbar'] = 'None' # Hide the toolbar

def initialize_grid(height, width, p=0.5):
    return np.random.choice([0, 1], size=(height, width), p=[1-p, p])

def display_grid(grid, fig, ax):
    ax.clear()  # Clear previous drawing
    ax.imshow(grid, cmap='binary')  # Display the grid
    plt.draw()

def update_grid(grid):
    new_grid = grid.copy()
    rows, cols = grid.shape

    for i in range(rows):
        for j in range(cols):
            # Calculate neighbors for cell (i, j)
            neighbors = grid[(i-1)%rows, j] + grid[(i+1)%rows, j] + \
                        grid[i, (j-1)%cols] + grid[i, (j+1)%cols] + \
                        grid[(i-1)%rows, (j-1)%cols] + grid[(i-1)%rows, (j+1)%cols] + \
                        grid[(i+1)%rows, (j-1)%cols] + grid[(i+1)%rows, (j+1)%cols]
            
            # Apply Game of Life rules
            if grid[i, j] == 1 and (neighbors < 2 or neighbors > 3):
                new_grid[i, j] = 0
            elif grid[i, j] == 0 and neighbors == 3:
                new_grid[i, j] = 1
    return new_grid

def reinitialize_patch(grid, height, width, patch_size=50, p=0.25, x=None, y=None):
    if x is None or y is None:
        x, y = np.random.randint(0, height-patch_size), np.random.randint(0, width-patch_size)
    grid[x:x+patch_size, y:y+patch_size] = initialize_grid(patch_size, patch_size, p=p)
    return grid

import numpy as np

def reinitialize_circle(grid, height, width, radius, p=0.25, center_x=None, center_y=None):
    
    if center_x is None or center_y is None:
        # If no center is provided, randomly choose a center
        center_x, center_y = np.random.randint(radius, width-radius), np.random.randint(radius, height-radius)
    
    # Iterate over a square bounding box around the circle
    for x in range(max(0, center_x-radius), min(width, center_x+radius+1)):
        for y in range(max(0, center_y-radius), min(height, center_y+radius+1)):
            # Calculate distance from the center
            distance = np.sqrt((x - center_x)**2 + (y - center_y)**2)
            # If the cell is within the circle, reinitialize based on probability p
            if distance <= radius:
                grid[y, x] = 1 if np.random.random() < p else 0
    return grid

def run_simulation(height, width):
    global grid, ani
    grid = initialize_grid(height, width)
    fig, ax = plt.subplots()
    plt.subplots_adjust(bottom=0.2)  # Adjust subplot to make room for the button

    # Generator function to update the grid
    def update_frame(num):
        global grid
        display_grid(grid, fig, ax)  # Display the current state of the grid
        grid = update_grid(grid)  # Update the grid to the next state
        return ax,

    frames=itertools.count()
    ani = animation.FuncAnimation(fig, update_frame, frames=frames, blit=False, interval=5, repeat=False)

    # Callbacks for play and stop buttons
    def play(event):
        ani.event_source.start()

    def stop(event):
        ani.event_source.stop()

    # Click event handler
    def onclick(event):
        # Convert click coordinates to grid coordinates
        ix, iy = int(event.xdata), int(event.ydata)
        # Check if click is within the grid bounds
        if 0 <= ix < width and 0 <= iy < height:
            # Reinitialize a patch at the click coordinates
            global grid
            grid = reinitialize_circle(grid, height, width, radius=10, p=0.25, center_x=ix, center_y=iy)

    # Connect the click event handler
    fig.canvas.mpl_connect('button_press_event', onclick)

    # Play button
    axplay = plt.axes([0.7, 0.05, 0.1, 0.075])
    bplay = Button(axplay, 'Play')
    bplay.on_clicked(play)

    # Stop button
    axstop = plt.axes([0.81, 0.05, 0.1, 0.075])
    bstop = Button(axstop, 'Stop')
    bstop.on_clicked(stop)

    plt.show()

# Parameters
width = 200
height = 120

run_simulation(height, width)