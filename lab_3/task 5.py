import turtle
from random import randint

number_of_turtle = 10
steps_of_the_time_number = 100
pool = [turtle.Turtle(shape='turtle') for i in range(number_of_turtle)]


def main():
    turtle_settings(pool)
    for i in range(steps_of_the_time_number):
        collision()


def turtle_settings(pool):
    """
    Put settings like size, speed, angel and start position in each turtle in the pool
    :param pool: list of turtle
    """
    for unit in pool:  # задаем каждой координаты, скорость, размер и угол поворота
        unit.turtlesize(0.4)
        unit.penup()
        unit.speed(randint(0, 10))
        unit.goto(randint(-200, 200), randint(-200, 200))
        unit.seth(randint(0, 360))


def atom_orientation(k):
    """
    Returns atom's angle, x and y position in tuple.
    :param k: index number of atom
    """
    angle = pool[k].heading()
    pos_x, pos_y = pool[k].pos()
    return angle, pos_x, pos_y


def collision():
    """
    Process the moment of collision and returns new angle for each atom
    :param i: index number for the first atom
    :param j: index number for the second atom
    :return:
    """
    for i in range(len(pool)):
        angle_i, x_i, y_i = atom_orientation(i)
        for j in range(len(pool)):
            if j != i:
                angle_j, x_j, y_j = atom_orientation(j)
                dx = abs(x_i - x_j)  # расстояние между координатами Х Г-ой и Х-ой(хетой) молекулой
                dy = abs(y_i - y_j)  # расстояние между координатами У Г-ой и Х-ой молекулой
                if dx <= 3 and dy <= 3:  # если расстояние меньше 3 (попали в одну клетку с диагональю 3*sqrt(2))
                    pool[j].seth(-angle_j)  # развернулась Х-ая молекула
                    pool[i].seth(-angle_i)  # развернулась Г-ая молекула
                    pool[i].fd(5)  # движение на 5 вперед, чтобы выйти из клетки
                    pool[j].fd(5)  # движение на 5 вперед, чтобы выйти из клетки
        bounce_from_border(i)
        move_forward(i)


def bounce_from_border(i):
    """
    Change atom orientation after collision with every border
    :param i:  atom index
    :return:
    """
    angle_i, x_i, y_i = atom_orientation(i)
    if x_i < -200 or x_i > 200:
        pool[i].seth(180 - angle_i)
    elif y_i < -200 or y_i > 200:
        pool[i].seth(-angle_i)


def move_forward(i):
    pool[i].fd(5)


main()
