import turtledraw as td
import math
td.set_turtlecfg(True)
td.set_filling(True)
td.set_animation(True)

HEIGHT = 600
h = HEIGHT
w =  h*2
diagonal = (w**2+h**2)**0.5
center = (0,0)

w_segs = 60
h_segs = 30
ws = w/w_segs
hs = h/h_segs

td.set_window('National Flag', width=w, height=h, bg='gray')

td.rect(center,w,h,colors='blue')

radoff = math.atan2(h,w)
degoff = 180 * radoff / math.pi

td.rect((0,0),diagonal,3*ws+3*hs,degoff,colors='white')
td.rect((0,0),diagonal,3*ws+3*hs,180-degoff,colors='white')

with td.Pen((0,0),colors='red',fill=True,animate=True) as t:
    t.setheading(degoff)
    t.forward(diagonal/2)
    t.left(90)
    t.forward(2*ws)
    t.left(90)
    t.forward(diagonal/2)
    t.left(90)
    t.forward(2*ws)

with td.Pen((0,0),colors='red',fill=True,animate=True) as t:
    t.setheading(degoff+180)
    t.forward(diagonal/2)
    t.left(90)
    t.forward(2*ws)
    t.left(90)
    t.forward(diagonal/2)
    t.left(90)
    t.forward(2*ws)

with td.Pen((0,0),colors='red',fill=True,animate=True) as t:
    t.setheading(180-degoff)
    t.forward(diagonal/2)
    t.left(90)
    t.forward(2*hs)
    t.left(90)
    t.forward(diagonal/2)
    t.left(90)
    t.forward(2*hs)

with td.Pen((0,0),colors='red',fill=True,animate=True) as t:
    t.setheading(360-degoff)
    t.forward(diagonal/2)
    t.left(90)
    t.forward(2*hs)
    t.left(90)
    t.forward(diagonal/2)
    t.left(90)
    t.forward(2*hs)

td.rect((0,0),w,10*hs,colors='white')
td.rect((0,0),10*ws,h,colors='white')

td.rect((0,0),w,6*hs,colors='red')
td.rect((0,0),6*ws,h,colors='red')

td.show()
