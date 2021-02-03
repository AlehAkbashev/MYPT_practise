from math import *
import pygame
from pygame.draw import *


def main(x, y):
    sky(x, y)
    seagull()
    water(x, y)
    bird(2*x/3, 0.2*y, 50, 0)
    bird(0.1*x, 0.005*y, 50, 15)
    bird(0.1*x, 0.3*y, 50, -15)
    fish()
    pass


def sky(x, y):
    rect(screen, DARK_BLUE, [0, 0, x, 0.1*y])
    rect(screen, ASPID_BLUE, [0, 0.1*y, x, 0.05*y])
    rect(screen, VIOLET_NEUT, [0, 0.15*y, x, 0.1*y])
    rect(screen, SALMON, [0, 0.25*y, x, 0.15*y])
    rect(screen, ORANGE, [0, 0.4*y, x, 0.1*y])


def bird(bird_x, bird_y, size, alpha):
    surf_size = (3*size, 2*size)
    surf_bird = pygame.Surface(surf_size)
    arc(surf_bird, WHITE, [1.5*size - 1, 0.5*size - size/3, 2*size/3, 2*size/3], pi/2, pi, 3)
    arc(surf_bird, WHITE, [1.5*size - 2*size/3 - 1, 0.5*size - size/3, 2*size, 4*size/3], atan(1 / 2), pi/2, 3)
    arc(surf_bird, WHITE, [1.5*size - 2*size/3 + 1, 0.5*size - size/3, 2*size/3, 2*size/3], 0, pi / 2, 3)
    arc(surf_bird, WHITE, [1.5*size - 4*size/3 + 1, 0.5*size - size/3, 2*size, 4*size/3], pi/2, pi - atan(1/2), 3)
    surf_bird.set_colorkey('black')
    surf_bird = pygame.transform.rotate(surf_bird, alpha)
    screen.blit(surf_bird, (bird_x, bird_y))
    pass

def seagull():
    pass

def water(x, y):
    rect(screen, TEAL, [0, 0.5*y, x, 0.5*y])

def fish():
    pass


pygame.init()

FPS = 30
x_scr, y_scr = 600, 800
scr_size = x_scr, y_scr
screen = pygame.display.set_mode(scr_size)

DARK_BLUE = (33, 33, 120)
ASPID_BLUE = (141, 95, 211)
VIOLET_NEUT = (205, 135, 222)
SALMON = (222, 135, 170)
ORANGE = (255, 153, 85)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
TEAL = (0, 102, 128)
BLUE = (0, 0, 255)
GREY_BLUE = (71, 136, 147)
GREY = (102, 99, 112)

main(x_scr, y_scr)

pygame.display.update()
clock = pygame.time.Clock()
finished = False
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
pygame.quit()

