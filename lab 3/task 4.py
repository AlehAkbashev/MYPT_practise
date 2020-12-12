import turtle

turtle.goto(500, 0)
turtle.goto(0, 0)
x = 0
y = 0
v_x = 10
v_y = 50
d_t = 0.05
t = 0
a_y = -9.81
while t < 100:
    x += v_x*d_t
    y += v_y*d_t + a_y*d_t**2/2
    v_y += a_y*d_t
    if y <= 0 and v_y < 0:
        v_y = -0.8 * v_y
        y = 0
    turtle.goto(x, y)

    t += d_t
