import turtle

def new_turtle(colors=None,show_drawing=False):
    t = turtle.Turtle()
    if isinstance(colors,str):
        pen_color = fill_color = colors
    elif isinstance(colors,tuple) or isinstance(colors,list):
        pen_color,fill_color = colors
    else:
        pen_color = fill_color = None
    if pen_color:
        t.pencolor(pen_color)
    if fill_color:
        t.fillcolor(fill_color)
    if not show_drawing:
        t.hideturtle()
        t.speed(0)
    return t
screen = turtle.Screen()
screen.tracer(0,0)
t1 = new_turtle(colors='red')
t1.begin_fill()
t1.circle(200,steps=800)
t1.end_fill()

t2 = new_turtle(colors='blue')
t2.begin_fill()
for _ in range(5):
    t2.forward(80)
    t2.right(144)
t2.end_fill()
screen.update()
turtle.done()
