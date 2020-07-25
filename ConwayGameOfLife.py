import pygame
import time
import copy

pygame.init()
pygame.display.set_caption("Conway's Game of Life")

square_size = 10
height = 50
width = 50

def setup(window):
    grid = [[0 for _ in range(width)] for _ in range(height)]
    end = False
    drag = False
    oldx, oldy = 0, 0
    while (not end):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    end = True
                    break
                if event.key == pygame.K_c:
                    grid = [[0 for _ in range(width)] for _ in range(height)]
            if event.type == pygame.MOUSEMOTION:
                if drag:
                    x = event.pos[0] // square_size
                    y = event.pos[1] // square_size
                    if (not (abs(oldx - x) == 0 and abs(oldy - y) == 0)):
                        grid[y][x] = 1 - grid[y][x]
                        oldx, oldy = x, y
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    drag = True
                    x = event.pos[0] // square_size
                    y = event.pos[1] // square_size
                    oldx, oldy = x, y
                    grid[y][x] = 1 - grid[y][x]
            elif event.type == pygame.MOUSEBUTTONUP:
                drag = False
        drawGrid(window, grid)
    return grid

def drawGrid(window, grid):
    for i in range(height):
        for j in range(width):
            if (grid[i][j] == 1): pygame.draw.rect(window, (0, 0, 0), (j * square_size, i * square_size, square_size, square_size))
            else: pygame.draw.rect(window, (255, 255, 255), (j * square_size, i * square_size, square_size, square_size))
            pygame.draw.rect(window, (230, 230, 230), (j * square_size, i * square_size, square_size, square_size), 1)
    pygame.display.update()

def getLiveNeighbors(grid, i, j):
    live_neighbors = 0
    for n in [-1, 0, 1]:
        for m in [-1, 0, 1]:
            if (not (n == 0 and m == 0)):
                if (0 <= i + n < height and 0 <= j + m < width):
                    if (grid[i + n][j + m] == 1):
                        live_neighbors += 1
    return live_neighbors

def update(grid):
    new_grid = copy.deepcopy(grid)
    for i in range(height):
        for j in range(width):
            live_neighbors = getLiveNeighbors(grid, i, j)

            if ((live_neighbors == 2 or live_neighbors == 3) and grid[i][j] == 1): new_grid[i][j] = 1
            elif (live_neighbors == 3 and grid[i][j] == 0): new_grid[i][j] = 1
            else: new_grid[i][j] = 0
    grid = copy.deepcopy(new_grid)
    del new_grid
    return grid

def main():
    window = pygame.display.set_mode((width * square_size, height * square_size))
    window.fill((255, 255, 255))
    grid = setup(window)
    paused = False
    delay = 0.05
    while (True):
        if (not paused):
            drawGrid(window, grid)
            grid = update(grid)
            time.sleep(delay)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    grid = setup(window)
                    break
                if event.key == pygame.K_p:
                    if (paused): paused = False
                    else: paused = True
                    break
                if event.key == pygame.K_RIGHT:
                    if (delay > 0.01): delay -= 0.01
                    break
                if event.key == pygame.K_LEFT:
                    delay += 0.01
                    break
    pygame.quit()

if __name__ == "__main__":
    main()