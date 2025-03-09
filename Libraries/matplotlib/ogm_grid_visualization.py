import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

#Creating a 4x4 grid, filled with 0.5 grey 
grid = np.full((4,4), 0.7)

# Display the grid
# cmap, sets the color map 
# vmin and max define the value range for the color scale, 0 is black and 1 is white

plt.imshow(grid, cmap = 'gray', vmin = 0, vmax=1)

# Add grid lines for better visibility 
plt.grid(visible = True, color = 'black', linewidth = 2)

# Set tick positions to align with cell borders
# np.arange(-0.5, 4, 1) sets tick marks starting at -0.5, ending at 3.5, with a step of 1
# Empty lists [] remove the numeric labels for cleaner visualization

plt.xticks(np.arange(-0.5,4,1), [])
plt.yticks(np.arange(-0.5,4,1), [])

# Add a red circle at cell (2, 2)
circle = Circle((2, 2), 0.3, color='red')
plt.gca().add_patch(circle)

plt.show()
