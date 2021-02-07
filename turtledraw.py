import turtle
import math

_TurtleCfg = None
_Fill = False
_Animation = True

class Pen(turtle.Turtle):
    def __init__(self,position=None,colors=None,fill=None,animate=None):
        if _TurtleCfg:
            self.turtle_visible = True
        else:
            self.turtle_visible = False
        super().__init__(visible=self.turtle_visible)
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
            self.speed(9)
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
        if self.turtle_visible:
            self.hideturtle()
        if not self.animate:
            self.getscreen().update()

def set_window(title='',width=None,height=None,bg=None):
    screen = turtle.Screen()
    screen.title(title)
    if width is None or height is None:
        screen.setup(width=0.5, height=0.5, startx=None, starty=None)
    else:
        woff,hoff = 4,4
        screen.setup(width+woff,height+hoff,None,None)
        screen.setworldcoordinates(-width/2+woff,-height/2-hoff,width/2+woff,height/2-hoff)
    if bg:
        screen.bgcolor(bg)

def set_turtlecfg(cfg):
    global _TurtleCfg
    _TurtleCfg = cfg

def set_filling(yn):
    global _Fill
    _Fill = yn

def set_animation(yn):
    global _Animation
    _Animation = yn

def show():
    turtle.done()

def star(center=(0,0),radius=10,degoff=90,*,colors=None,fill=None,animate=None):
    """
    center: the center point coordinate (x,y) in the star 
    defoff: initial heading degree , anticlockwise rotated from east direction
    radius: distance between center and the star vertex
    """
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


def rect(center=(0,0),width=10,height=10,degoff=0,*,colors=None,fill=None,animate=None):
    with Pen(center,colors,fill,animate) as t:
        t.setheading(degoff)
        t.penup()
        t.forward(width/2)
        t.left(90)
        t.forward(height/2)
        t.left(90)
        t.pendown()
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
        
def line(start=(0,0),length=10,degoff=0,*,colors,animate):
    fill = False
    with Pen(start,colors,fill,animate) as t:
        t.setheading(degoff)
        t.forward(length)

def line2(start=(0,0),end=(10,10),*,colors=None,animated=None):
    with Pen(start,colors,animate=None) as t:
        t.goto(end)

def circle(center,radius,degoff=0,extent=None,*,colors=None,fill=None,animate=None):
    with Pen(center,colors,fill,animate) as t:
        t.penup()
        t.setheading(degoff)
        t.forward(radius)
        t.left(90)
        t.pendown()
        start = t.pos()
        t.circle(radius,extent)
        if extent is not None:
            t.goto(center)
            t.goto(start)
        else:
            t.penup()
            t.goto(center)
            t.pendown()

def grid(center=(0,0),width=10,height=10,rows=2,cols=2,degoff=0,*,colors=None,animate=None):
    fill = False
    row_width = height/rows
    col_width = width/cols
    rect(center,width,height,degoff,colors=colors,fill=fill,animate=animate)
    with Pen(center,colors,fill,animate) as t:
        t.setheading(degoff)
        t.penup()
        t.backward(width/2)
        t.right(90)
        t.backward(height/2)
        t.pendown()
        pos = t.pos()
        for _ in range(rows-1):
            t.penup()
            t.forward(row_width)
            t.left(90)
            t.pendown() 
            t.forward(width)
            t.penup()
            t.backward(width)
            t.right(90)
            t.pendown()
        t.penup()
        t.goto(pos)
        t.pendown()
        t.setheading(degoff)
        for _ in range(cols-1):
            t.penup()
            t.forward(col_width)
            t.right(90)
            t.pendown()
            t.forward(height)
            t.penup()
            t.backward(height)
            t.left(90)
            t.pendown()
        t.penup()
        t.goto(center)
        t.pendown()

def poly(first=(0,0),second=(10,10),third=(10,0),*rest_points,colors=None,fill=None,animate=None):
    with Pen(first,colors,fill,animate) as t:
        t.goto(second)
        t.goto(third)
        for p in rest_points:
            t.goto(p)
        t.goto(first)

if __name__ == '__main__':
    pass 


