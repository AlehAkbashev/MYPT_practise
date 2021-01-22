from math import *
import pygame
from pygame.draw import *


def main():
    sky()
    birds()
    seagull()
    water()
    fish()
    pass


def sky():
    pass


def birds():
    pass

def seagull():
    pass

def water():
    pass

def fish():
    pass


pygame.init()

FPS = 30
x_scr, y_scr = 600, 800
scr_size = x_scr, y_scr
screen = pygame.display.set_mode(scr_size)

main()

pygame.display.update()
clock = pygame.time.Clock()
finished = False
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
pygame.quit()

