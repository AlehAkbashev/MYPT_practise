import turtle

mail_numbers = [
    (   # 0
        'turtle.pendown()', 'turtle.forward(25)', 'turtle.right(90)', 'turtle.forward(50)', 'turtle.right(90)',
        'turtle.forward(25)', 'turtle.right(90)', 'turtle.forward(50)', 'turtle.penup()', 'turtle.right(90)',
        'turtle.forward(25)', 'turtle.forward(50)'
    ),
    (   # 1
        'turtle.right(90)', 'turtle.forward(25)', 'turtle.pendown()', 'turtle.left(135)', 'turtle.forward(35.35)',
        'turtle.right(135)', 'turtle.forward(50)', 'turtle.penup()', 'turtle.left(180)', 'turtle.forward(50)',
        'turtle.right(90)', 'turtle.forward(50)'
    ),
    (   # 2
        'turtle.pendown()', 'turtle.forward(25)', 'turtle.right(90)', 'turtle.forward(25)', 'turtle.right(90)',
        'turtle.forward(25)', 'turtle.left(90)', 'turtle.forward(25)', 'turtle.left(90)', 'turtle.forward(25)',
        'turtle.penup()', 'turtle.left(90)', 'turtle.forward(50)', 'turtle.right(90)', 'turtle.forward(50)'
    ),
    (   # 3
        'turtle.pendown()', 'turtle.forward(25)', 'turtle.right(90)', 'turtle.forward(25)', 'turtle.right(90)',
        'turtle.forward(25)', 'turtle.back(25)', 'turtle.left(90)', 'turtle.forward(25)', 'turtle.right(90)',
        'turtle.forward(25)', 'turtle.back(25)', 'turtle.right(90)', 'turtle.penup()', 'turtle.forward(50)',
        'turtle.right(90)', 'turtle.forward(50)'
    ),
    (   # 4
        'turtle.pendown()', 'turtle.right(90)', 'turtle.forward(25)', 'turtle.left(90)', 'turtle.forward(25)',
        'turtle.right(90)', 'turtle.forward(25)', 'turtle.back(50)', 'turtle.penup()', 'turtle.left(90)',
        'turtle.forward(50)'
    ),
    (   # 5
        'turtle.pendown()', 'turtle.penup()', 'turtle.right(90)', 'turtle.forward(50)', 'turtle.pendown()',
        'turtle.left(90)', 'turtle.forward(25)', 'turtle.left(90)', 'turtle.forward(25)', 'turtle.left(90)',
        'turtle.forward(25)', 'turtle.right(90)', 'turtle.forward(25)', 'turtle.right(90)', 'turtle.forward(25)',
        'turtle.penup()', 'turtle.forward(50)'
    ),
    (   # 6
        'turtle.right(90)', 'turtle.forward(25)', 'turtle.left(90)', 'turtle.pendown()', 'turtle.forward(25)',
        'turtle.right(90)', 'turtle.forward(25)', 'turtle.right(90)', 'turtle.forward(25)', 'turtle.right(90)',
        'turtle.forward(50)', 'turtle.right(90)', 'turtle.forward(25)', 'turtle.penup()', 'turtle.forward(50)'
    ),
    (   # 7
        'turtle.right(90)', 'turtle.forward(50)', 'turtle.pendown()', 'turtle.back(25)', 'turtle.right(45)',
        'turtle.back(35.35)', 'turtle.left(135)', 'turtle.back(25)', 'turtle.penup()', 'turtle.forward(75)'
    ),
    (   # 8
        'turtle.right(90)', 'turtle.forward(25)', 'turtle.left(90)',
        'turtle.pendown()', 'turtle.forward(25)', 'turtle.right(90)',
        'turtle.forward(25)', 'turtle.right(90)', 'turtle.forward(25)',
        'turtle.right(90)', 'turtle.forward(50)', 'turtle.right(90)',
        'turtle.forward(25)', 'turtle.right(90)', 'turtle.forward(25)',
        'turtle.penup()', 'turtle.back(25)', 'turtle.left(90)',
        'turtle.forward(50)'
    ),
    (   # 9
        'turtle.right(90)', 'turtle.forward(50)', 'turtle.right(45)', 'turtle.pendown()', 'turtle.back(35.35)',
        'turtle.right(45)', 'turtle.forward(25)', 'turtle.right(90)', 'turtle.forward(25)', 'turtle.right(90)',
        'turtle.forward(25)', 'turtle.right(90)', 'turtle.forward(25)', 'turtle.penup()', 'turtle.back(25)',
        'turtle.left(90)', 'turtle.forward(50)'
    )
]

my_index = input()
turtle.penup()
turtle.goto(-200, 0)
for number in my_index:
    for draw_rule in mail_numbers[int(number)]:
        eval(draw_rule)
