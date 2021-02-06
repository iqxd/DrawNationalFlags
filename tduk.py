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
ws_hy = ws / math.sin(radoff)
degoff = 180 * radoff / math.pi
hs_hy = hs / math.sin(math.pi/2- radoff)

td.rect((0,0),diagonal,3*ws+3*hs,degoff,colors='white')
td.rect((0,0),diagonal,3*ws+3*hs,180-degoff,colors='white')

upleft = (w/2,h/2)
downright = (-w/2,-h/2)
td.line2(upleft,downright)
for i in range(1,4):
    td.line2((upleft[0]-ws_hy*i,upleft[1]),(downright[0],downright[1]+hs_hy*i))
    td.line2((upleft[0],upleft[1]-hs_hy*i),(downright[0],downright[1]+hs_hy*i))

upright = (-w/2,h/2)
downleft = (w/2,-h/2)
td.line2(upright,downleft)
for i in range(1,4):
    td.line2((upright[0]+ws_hy*i,upleft[1]),(downright[0],downright[1]+hs_hy*i))
    td.line2((upright[0],upleft[1]-hs_hy*i),(downright[0]-ws_hy*i,downright[1]))


# with td.Pen((0,0),colors='red',fill=True,animate=True) as t:
#     t.setheading(degoff)
#     t.forward(diagonal/2)
#     t.left(90)
#     t.forward(2*ws)
#     t.left(90)
#     t.forward(diagonal/2)
#     t.left(90)
#     t.forward(2*ws)

# with td.Pen((0,0),colors='red',fill=True,animate=True) as t:
#     t.setheading(degoff+180)
#     t.forward(diagonal/2)
#     t.left(90)
#     t.forward(2*ws)
#     t.left(90)
#     t.forward(diagonal/2)
#     t.left(90)
#     t.forward(2*ws)

# with td.Pen((0,0),colors='red',fill=True,animate=True) as t:
#     t.setheading(180-degoff)
#     t.forward(diagonal/2)
#     t.left(90)
#     t.forward(2*hs)
#     t.left(90)
#     t.forward(diagonal/2)
#     t.left(90)
#     t.forward(2*hs)

# with td.Pen((0,0),colors='red',fill=True,animate=True) as t:
#     t.setheading(360-degoff)
#     t.forward(diagonal/2)
#     t.left(90)
#     t.forward(2*hs)
#     t.left(90)
#     t.forward(diagonal/2)
#     t.left(90)
#     t.forward(2*hs)

td.rect((0,0),w,10*hs,colors='white')
td.rect((0,0),10*ws,h,colors='white')

td.rect((0,0),w,6*hs,colors='red')
td.rect((0,0),6*ws,h,colors='red')

td.show()
