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
    x_eye_left = x_face - face_radius / 2
    y_eye_left = y_face - 0.1 * face_radius
    x_eye_right = x_face + face_radius / 2
    y_eye_right = y_face - 0.1 * face_radius
    # right eye
    circle(screen, RED, (x_eye_right, y_eye_right), eye_radius / 2)
    circle(screen, BLACK, (x_eye_right, y_eye_right), eye_radius / 2, 1)
    circle(screen, BLACK, (x_eye_right, y_eye_right), eye_radius / 4)
    # left eye
    circle(screen, RED, (x_eye_left, y_eye_left), eye_radius)
    circle(screen, BLACK, (x_eye_left, y_eye_left), eye_radius, 1)
    circle(screen, BLACK, (x_eye_left, y_eye_left), eye_radius / 2)


def eyebrows(x_face, y_face, r, alpha, beta):
    eye_rad = r * 0.2
    x_touch_p_left = x_face - r / 2 + eye_rad * cos(alpha * pi / 180)
    y_touch_p_left = y_face - 0.1 * r - eye_rad * sin(alpha * pi / 180)
    k_left = tan((90 - alpha) * pi / 180)
    b_left = y_touch_p_left - k_left * x_touch_p_left
    brow_len = r
    # x1, y1 - coordinates for the left side of left eyebrow
    x1_left = x_touch_p_left - brow_len * cos((90 - alpha) * pi / 180)
    y1_left = k_left * x1_left + b_left
    # x2, y2 - coordinates for the right side of left eyebrow
    x2_left = x_touch_p_left + 0.5 * eye_rad
    y2_left = k_left * x2_left + b_left
    k1_left = tan(alpha * pi / 180)
    brow_wide = eye_rad / 2
    y_wide_left = brow_wide * sin(alpha * pi / 180)
    x_wide_left = brow_wide * cos(alpha * pi / 180)
    polygon(screen, BLACK,
            (
                (x1_left, y1_left),
                (x2_left, y2_left),
                (x2_left + x_wide_left, y2_left - y_wide_left),
                (x1_left + x_wide_left, y1_left - y_wide_left)
            )
            )
    x_touch_p_right = x_face + r/2 + eye_rad/2 * cos(beta*pi/180)
    y_touch_p_right = y_face - 0.1 * r - eye_rad/2*sin(beta*pi/180)
    k_right = tan((270 - beta) * pi / 180)
    b_right = y_touch_p_right - k_right * x_touch_p_right
    x1_right = x_touch_p_right - 0.5 * eye_rad
    y1_right = x1_right * k_right + b_right
    x2_right = x_touch_p_right + brow_len * cos((beta-90)*pi/180)
    y2_right = x2_right * k_right + b_right
    y_wide_right = brow_wide * sin((180 - beta)*pi/180)
    x_wide_right = brow_wide * cos((180 - beta)*pi/180)
    polygon(screen, BLACK, ((x1_right, y1_right),
                            (x2_right, y2_right),
                            (x2_right - x_wide_right, y2_right - y_wide_right),
                            (x1_right - x_wide_right, y1_right - y_wide_right)
                            )
            )


def mouth(x_face, y_face, face_radius):
    x1 = x_face - face_radius / 2
    x2 = x_face + face_radius / 2
    wide = face_radius * 0.2
    y1 = y_face + 2*face_radius / 3
    rect(screen, BLACK, (x1, y1-wide, x2-x1, wide))
    

def main():
    x_face, y_face = 300, 300
    r = 200
    alpha, beta = 45, 120
    eye_rad = 0.2 * r
    face(x_face, y_face, r)
    eyes(x_face, y_face, r, eye_rad)
    eyebrows(x_face, y_face, r, alpha, beta)
    mouth(x_face, y_face, r)


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
