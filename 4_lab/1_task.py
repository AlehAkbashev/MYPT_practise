from math import *
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


def eyes(x_face, y_face, face_radius, eye_radius):
    x_eye_left = x_face - face_radius/2
    y_eye_left = y_face - 0.1*face_radius
    x_eye_right = x_face + face_radius/2
    y_eye_right = y_face - 0.1 * face_radius
    # right eye
    circle(screen, RED, (x_eye_right, y_eye_right), eye_radius/2)
    circle(screen, BLACK, (x_eye_right, y_eye_right), eye_radius/2, 1)
    circle(screen, BLACK, (x_eye_right, y_eye_right), eye_radius / 4)
    # left eye
    circle(screen, RED, (x_eye_left, y_eye_left), eye_radius)
    circle(screen, BLACK, (x_eye_left, y_eye_left), eye_radius, 1)
    circle(screen, BLACK, (x_eye_left, y_eye_left), eye_radius / 2)


def eyebrows(x_face, y_face, r):
    eye_rad = r * 0.2
    alpha = 45

    x_touch_p = x_face - r / 2 + eye_rad * cos(alpha*pi/180)
    y_touch_p = y_face - 0.1 * r - eye_rad * sin(alpha*pi/180)
    k = tan((90 - alpha) * pi / 180)
    b = y_touch_p - k * x_touch_p
    brow_len = r
    # x1, y1 - coordinates for the left side of left eyebrow
    x1 = x_touch_p - brow_len * cos((90 - alpha) * pi / 180)
    y1 = k * x1 + b
    # x2, y2 - coordinates for the right side of left eyebrow
    x2 = x_touch_p + 0.5 * eye_rad
    y2 = k * x2 + b
    k1 = tan(alpha*pi/180)
    brow_wide = eye_rad / 2
    y_wide = brow_wide * sin(alpha*pi/180)
    x_wide = brow_wide * cos(alpha*pi/180)
    polygon(screen, BLACK, (
        (x1, y1),
        (x2, y2),
        (x2 + x_wide, y2 - y_wide),
        (x1 + x_wide, y1 - y_wide)
    )
            )

    pass


def main():
    x_face, y_face = 300, 300
    r = 200
    eye_rad = 0.2 * r
    face(x_face, y_face, r)
    eyes(x_face, y_face, r, eye_rad)
    eyebrows(x_face, y_face, r)


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
