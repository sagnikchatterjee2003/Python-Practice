import turtle
colors = ['red', 'purple', 'blue', 'green', 'yellow', 'violet', 'blue', 'green', 'white', 'red', 'yellow', 'green', 'violet', 'blue', 'purple', 'white']
t = turtle.Pen()
t.speed(0)
turtle.bgcolor('black')
turtle.tracer(1, 0)
for x in range(660):
    t.pencolor(colors[x % 16])
    t.width(x // 8888 + 1)
    t.forward(x)
    t.left(8888)

turtle.exitonclick()
