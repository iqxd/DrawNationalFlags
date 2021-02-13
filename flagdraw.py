from turtle import _Screen, RawTurtle, Screen, mainloop,Vec2D
import math
from typing import Union,Optional


class Canvas:
    screen: _Screen
    guider: RawTurtle
    painter: RawTurtle
    animate: bool

    def __init__(self,
                 title: str,
                 width: int,
                 height: int,
                 bgcolor: str = 'gray',
                 animate: bool = True) -> None:
        screen = Screen()
        screen.title(title)
        screen.setup(width + 20, height + 20)
        screen.bgcolor(bgcolor)
        guider = RawTurtle(screen, 'classic', 1000, True)
        guider.color('black')
        painter = RawTurtle(screen, 'circle', 1000, True)
        if animate:
            guider.speed(9)
            painter.speed(9)
            screen.tracer(1, 15)
        else:
            guider.speed(0)
            painter.speed(0)
            screen.tracer(0, 0)
        self.screen = screen
        self.guider = guider
        self.painter = painter
        self.animate = animate

    def move(self,draw=None,*actions):
        """
        action type (
        draw :  None pepup, (color,None) nofill, color | (color,color) fill
        coordinate : Vec2D , use goto function
        turndegree: tuple[str, int | float] , turn 'd' degree or 'r' radian , positive right, negative left
        distance : int | float, positive forward , negative backward )
        """
        if draw:
            if isinstance(draw,tuple) and draw[1] is None:
                t = self.guider
                t.color(draw[0])
            else:
                t = self.painter 
                t.color(draw)
        else:
            t = self.guider
        
        if t==self.painter:
            t.begin_fill()

        for a in actions:
            if isinstance(a,tuple):
                if a[0] == 'd':
                    if a[1]>=0:
                        t.right(a[1])
                    else:
                        t.left(a[1])
                elif a[0] == 'r':
                    ...
                else:
                    t.goto(a)
            else:
                if a>=0:
                    t.forward(a)
                else:
                    t.backward(-a)

        if t == self.painter:
            t.end_fill()
                    

    def line(self,start:Vec2D,rotate_or_end:Union[int,float,Vec2D],length:Union[int,float,None]=None):
        t = self.guider
        t.penup()
        t.goto(start)
        t.pendown()
        if isinstance(rotate_or_end,int) or isinstance(rotate_or_end,float):
            t.setheading(rotate_or_end)
            t.forward(length)
        else:
            t.goto(rotate_or_end)
        

    def rect(self,center:Vec2D,
            width:Union[int,float],
            height:Union[int,float],
            rotate:Union[int,float],
            fillcolor:Optional[str]=None)->None:
        t = self.painter if fillcolor else self.guider
        if fillcolor:
            t.color(fillcolor)
            t.begin_fill()
        t.penup()
        t.goto(center)
        t.setheading(rotate)
        t.forward(width/2)
        t.pendown()
        t.right(90)
        t.forward(height/2)
        t.right(90)
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)
        t.forward(width)
        t.right(90)
        t.forward(height/2)
        if fillcolor:
            t.end_fill()

    def hideguider(self):
        self.guider.hideturtle()

    def hidepainter(self):
        self.painter.hideturtle()

    def finish(self) -> None:
        self.hidepainter()
        for _ in range(self.guider.undobufferentries()):
            self.guider.undo()
        self.hideguider()
        if not self.animate:
            self.screen.update()
        mainloop()


if __name__ == '__main__':
    f = Canvas('test', 500, 500)
    f.rect((50,50),200,150,10,'cyan')
    f.move('red',(0,0),(50,0),('d',45),100)
    f.finish()
