import turtle
import math

_Fill = False
_Animation = True

class Pen(turtle.Turtle):
    def __init__(self,position=None,colors=None,fill=None,animate=None,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.hideturtle()
        self.position = position
        self.fill = fill
        self.animate = animate
        if self.position:
            self.penup()
            self.goto(*self.position)
            self.pendown()
        if isinstance(colors,str):
            pen_color = fill_color = colors
        elif isinstance(colors,tuple) or isinstance(colors,list):
            pen_color,fill_color = colors
        else:
            pen_color = fill_color = None
        if pen_color:
            self.pencolor(pen_color)
        if fill_color:
            self.fillcolor(fill_color)
        if fill is None:
            self.fill = _Fill
        if animate is None:
            self.animate = _Animation

    def __enter__(self):
        if self.animate:
            self.speed(0)
            self.getscreen().tracer(1,25)
        else:
            self.speed(0)
            self.getscreen().tracer(0,0)
        if self.fill:
            self.begin_fill()
        return self

    def __exit__(self,exc_type,exc_val,exc_tb):
        if self.fill:
            self.end_fill()
        if not self.animate:
            self.getscreen().update()

def set_window(title='',width=None,height=None,bg=None):
    screen = turtle.Screen()
    screen.title(title)
    if width is None or height is None:
        screen.setup(width=0.5, height=0.5, startx=None, starty=None)
    else:
        screen.setup(width,height,None,None)
    if bg:
        screen.bgcolor(bg)

def set_filling(yn):
    global _Fill
    _Fill = yn

def set_animation(yn):
    global _Animation
    _Animation = yn

def show():
    turtle.done()

def star(center,degoff,radius,*,colors=None,fill=None,animate=None):
    sidelen = 2*radius*math.cos(0.1*math.pi)
    with Pen(center,colors,fill,animate) as t:
        t.setheading(degoff)
        t.penup()
        t.forward(radius)
        t.pendown()
        t.left(162)
        for _ in range(5):
            t.forward(sidelen)
            t.left(144)
        t.penup()
        t.goto(center)
        t.pendown()


def rect(center,width,height,colors=None,fill=None,animate=None):
    with Pen(center,colors,fill,animate) as t:
        t.penup()
        t.goto(center[0]+width/2,center[1]+height/2)
        t.pendown()
        t.setheading(180)
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.penup()
        t.goto(center)
        t.pendown()
        

