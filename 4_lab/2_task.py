from math import *
import pygame
from pygame.draw import *


def main(x, y):
    sky(x, y)
    water(x, y)
    bird(2*x/3, 0.2*y, 50, 0)
    bird(0.1*x, 0.005*y, 50, 15)
    bird(0.1*x, 0.3*y, 50, -15)
    seagull(3*x/7, 0.75*y, 3*x/4)
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


def seagull(x_c, y_c, size):
    body_x = x_c
    body_y = y_c
    body_size = size / 3
    body(body_x, body_y, body_size)
    neck_size = body_size / 2
    neck_x = body_x + body_size/2 + 0.15*neck_size
    neck_y = body_y - 0.4 * neck_size/4
    neck_n_head(neck_x, neck_y, neck_size)

    leg()
    tail()
    wing()
    pass


def body(x, y, size):
    ellipse(screen, WHITE, [x-size/2, y-size/4, size, size/2])
    pass


def neck_n_head(x, y, size):
    ellipse(screen, WHITE, [x - size / 2, y - size / 4, size, size / 2])
    head_size = size * 0.75
    head_x = x + size / 2 + head_size / 10
    head_y = y - size / 4
    head_size_x = head_size
    head_size_y = 0.65*head_size
    head(head_x, head_y, head_size_x, head_size_y)
    eye_size = head_size * 0.2
    eye_x = head_x + head_size/4
    eye_y = head_y - head_size/8
    eye_size_x = eye_size
    eye_size_y = 0.65*eye_size
    eye(eye_x, eye_y, eye_size_x, eye_size_y)
    pass


def head(x, y, size_x, size_y):
    ellipse(screen, WHITE, [x - size_x/2, y - size_y/2, size_x, size_y])


def eye(x, y, size_x, size_y):
    ellipse(screen, BLACK, [x - size_x/2, y - size_y/2, size_x, size_y])

def leg():
    pass

def tail():
    pass

def wing():
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

