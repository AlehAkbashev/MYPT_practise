import pygame
from pygame.draw import *

pygame.init()

FPS = 30
x, y = 800, 600
scr_size = (x, y)

screen = pygame.display.set_mode(scr_size)


YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

screen.fill(WHITE)


def face(x_cent, y_cent, radius):
    circle(screen, YELLOW, (x_cent, y_cent), radius)
    circle(screen, BLACK, (x_cent, y_cent), radius, 3)


def eyes(x_eye, y_eye, face_radius, eye_radius, side):
    circle(screen, RED, (x_eye + face_radius / 2, y_eye - 0.1 * face_radius), eye_radius / 2)
    circle(screen, BLACK, (x_eye + face_radius / 2, y_eye - 0.1 * face_radius), eye_radius / 2, 1)
    circle(screen, BLACK, (x_eye + face_radius / 2, y_eye - 0.1 * face_radius), eye_radius / 4)
    circle(screen, RED, (x_eye - face_radius / 2, y_eye - 0.1 * face_radius), eye_radius)
    circle(screen, BLACK, (x_eye - face_radius / 2, y_eye - 0.1 * face_radius), eye_radius, 1)
    circle(screen, BLACK, (x_eye - face_radius / 2, y_eye - 0.1 * face_radius), eye_radius / 2)


def main():
    x_face, y_face = 300, 300
    r = 200
    face(x_face, y_face, r)
    eyes(x_face, y_face, r, 0.2 * r)

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
