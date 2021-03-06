import random
import sys

import pygame

from colours import dark_blue, green, black

def draw_grid():
    for x in range(0, width, cell_size):
        pygame.draw.line(screen, dark_blue, (x, 0), (x, height))
    for y in range(0, height, cell_size):
        pygame.draw.line(screen, dark_blue, (0, y), (width, y))

def draw_cells():
    for (x, y) in cells:
        colour = green if cells[x, y] else black
        rectangle = (x * cell_size, y * cell_size, cell_size, cell_size)
        pygame.draw.rect(screen, colour, rectangle)

def get_neighbours((x, y)):
    positions = [(x - 1, y - 1), (x, y - 1), (x + 1, y - 1), (x + 1, y),
                 (x + 1, y + 1), (x, y + 1), (x - 1, y + 1), (x - 1, y)]
    return [cells[r, c] for (r, c) in positions if 0 <= r < rows and 0 <= c < columns]

def evolve():
    for position, alive in cells.items():
        live_neighbours = sum(get_neighbours(position))
        if alive:
            if live_neighbours < 2 or live_neighbours > 3:
                cells[position] = False
        elif live_neighbours == 3:
                cells[position] = True


def get_cells(cells):
    blank_board = {(c, r): (c, r) in cells for c in range(columns) for r in range(rows)}
    return blank_board


block = {(1, 1), (1, 2),
         (2, 1), (2, 2)}


beehive = {(5, 1), (6, 1),
        (4, 2),         (7, 2),
            (5, 3), (6, 3)}

loaf = {(5, 1), (6, 1),
    (4, 2),         (7, 2),
        (5, 3),     (7, 3),
            (6, 4)}

boat = {(4, 1), (5, 1),
        (4, 2),     (6, 2),
            (5, 3)}

blinker = {(5, 2), (6, 2), (7, 2)}


pygame.init()


columns, rows = 50, 50
cells = get_cells(blinker)
clock = pygame.time.Clock()
speed = 1

cell_size = 10
size = width, height = columns * cell_size, rows * cell_size
screen = pygame.display.set_mode(size)


while True:
    clock.tick(speed)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if speed > 1 and event.key == pygame.K_LEFT:
                speed -= 1
            if event.key == pygame.K_RIGHT:
                speed += 1
    draw_cells()
    evolve()
    draw_grid()

    pygame.display.update()