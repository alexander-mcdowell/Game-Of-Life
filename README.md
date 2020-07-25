# Game-Of-Life
My attempt at recreating Conway's Game of Life in python, written using pygame 1.9.6 and python 3.6.10.

To play the game, simply run ```python ConwayGameOfLife.py``` in your terminal of choice (pygame must be installed for the program to run).

Rules of Conway's Game of Life:
- Cells of a grid are either "dead" or "alive" and are marked with either a white or black box respectively.
- For each cell, count the number of neighbors it has and following the following instructions:
    - Any live cell with two or three live neighbours survives.
    - Any dead cell with three live neighbours becomes a live cell.
    - All other live cells die in the next generation.
    - All other dead cells stay dead.

Controls:
- Left mouse click/drag: Only works in "drawing mode". Changes whether a cell at the current mouse position is alive or dead.
- Return/Enter: Toggles between "drawing mode" and "running mode". Cells only start following the rules of the game in running mode and new cells cannot be added in running mode.
- C: Clears the screen in "drawing mode".
- P: Pauses time in "running mode".
- Left arrow: Slows time down in "running mode".
- Right attow: Speeds time up in "running mode".

The game window can only be closed by hitting the X button or by typing Crtl + Z in the terminal window.
