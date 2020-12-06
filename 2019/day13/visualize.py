import pygame
import math
import sys
sys.path.insert(1, '..')
from intcode.computer import IntcodeComputer
pygame.init()

# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)

WIDTH = 360
HEIGHT = 210
size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Intcode Breakout")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

with open('./input') as file:
    raw = file.read()
    raw_list = [int(i) for i in raw.split(",")]

program_list = [0] * len(raw_list) * 10

for i in range(len(raw_list)):
    program_list[i] = raw_list[i]

program_list[0] = 2
comp = IntcodeComputer(program_list)
blocks = set()
score = -1
paddle_x = 10
ball_x = 0
ball_y = -1
joystick = 0
last_tile = -1
grid = [[BLACK] * 50 for _ in range(50)]
WALL = WHITE
BLANK = BLACK
BALL = RED
BRICK = BLUE
PADDLE = GREEN

painted = False
while not painted:
    if last_tile == 4:
        comp.queue_input(joystick)
    x = comp.run()
    y = comp.run()
    tile = comp.run()

    if tile == 2:
        grid[y][x] = BRICK
        blocks.add((x,y))
    elif tile == 4 and (x,y) in blocks:
        blocks.remove((x,y))
    elif tile == 3:
        painted = True
        grid[y][x] = PADDLE
        paddle_x = x
        if paddle_x == 34:
            joystick = -1
    elif tile == 4:
        grid[y][x] = BALL
        ball_x = x
        ball_y = y

        diff = ball_x - paddle_x
        if diff != 0:
            joystick = diff // abs(diff)
        else:
            joystick = 0
    elif x == -1 and y == 0:
        score = tile
    elif tile == 1:
        grid[y][x] = WALL
    elif tile == 0:
        grid[y][x] = BLANK
    last_tile = tile

# -------- Main Program Loop -----------
while comp.index >= 0 and not done:
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

    # step of the simulation
    if last_tile == 4:
        comp.queue_input(joystick)
    x = comp.run()
    y = comp.run()
    tile = comp.run()

    if tile == 2:
        grid[y][x] = BRICK
        blocks.add((x,y))
    elif tile == 4 and (x,y) in blocks:
        blocks.remove((x,y))
    elif tile == 3:
        grid[y][x] = PADDLE
        paddle_x = x
        if paddle_x == 34:
            joystick = -1
    elif tile == 4:
        grid[y][x] = BALL
        ball_x = x
        ball_y = y

        diff = ball_x - paddle_x
        if diff != 0:
            joystick = diff // abs(diff)
        else:
            joystick = 0
    elif x == -1 and y == 0:
        score = tile
    elif tile == 1:
        grid[y][x] = WALL
    elif tile == 0:
        grid[y][x] = BLANK

    last_tile = tile

    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(WHITE)

    for x in range(len(grid[0])):
        for y in range(len(grid)):
            color = grid[y][x]
            # screen.set_at((x, y), color)
            pygame.draw.rect(screen, color, [10 * x, 10 * y, 10, 10])


    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

pygame.quit()

