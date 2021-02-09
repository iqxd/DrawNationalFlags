from turtle import _Screen, RawTurtle, Screen, mainloop
import math
from typing import Union


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

    def finish(self) -> None:
        self.guider.hideturtle()
        self.painter.hideturtle()
        if not self.animate:
            self.screen.update()
        mainloop()


if __name__ == '__main__':
    f = Canvas('test', 500, 500)
    f.guider.circle(100)
    f.painter.forward(200)
    f.finish()
