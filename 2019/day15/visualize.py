import pygame
import math
import sys
from main import Day15Runner
pygame.init()

# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)

WIDTH = 300
HEIGHT = 300
size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Intcode Maze")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

grid = [[BLACK] * 80 for _ in range(50)]
runner = Day15Runner()
OFFSET = 25
mapped_rest = False

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pass
        elif event.type == pygame.MOUSEBUTTONUP:
            pass
        elif event.type == pygame.MOUSEMOTION:
            pass

    if not runner.completed:
        result, pos = runner.do_step()

        if result == 0:
            grid[pos[0] + OFFSET][pos[1] + OFFSET] = WHITE
        elif result == 1:
            grid[pos[0] + OFFSET][pos[1] + OFFSET] = RED
        else:
            grid[pos[0] + OFFSET][pos[1] + OFFSET] = BLUE
    elif not mapped_rest:
        runner.map_unknowns()
        mapped_rest = True
        for pos in runner.walls:
            grid[pos[0] + OFFSET][pos[1] + OFFSET] = WHITE
        for pos in runner.visited:
            grid[pos[0] + OFFSET][pos[1] + OFFSET] = GREEN
    elif not runner.oxygen_complete:
        runner.do_oxygen_step()
        for pos in runner.oxygenated:
            grid[pos[0] + OFFSET][pos[1] + OFFSET] = BLUE


    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(WHITE)

    for x in range(len(grid[0])):
        for y in range(len(grid)):
            color = grid[y][x]
            # screen.set_at((x, y), color)
            pygame.draw.rect(screen, color, [5 * x, 5 * y, 5, 5])


    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(160)

pygame.quit()

