import turtledraw as td
import math
td.set_turtlecfg(True)
td.set_filling(True)
td.set_animation(True)

HEIGHT = 600
h = HEIGHT
wh_ratio = 1.5
w =  h*wh_ratio
diagonal = (w**2+h**2)**0.5
center = (0,0)

w_segs = 72
h_segs = 48
seg =math.sqrt(((w/w_segs)**2+(h/h_segs)**2)/2)
bc_radius = 12*seg
sc_radius = 6*seg
wr = 12*seg
hr = 8*seg
br = 2*seg
gr = 1*seg

td.set_window('National Flag', width=w, height=h, bg='gray')

td.rect(center,w,h,colors='white')

td.line2((w/2,h/2),(-w/2,-h/2),colors='black')
td.line2((-w/2,h/2),(w/2,-h/2),colors='black')
td.circle((0,0),radius=bc_radius,fill=False,colors='black')

radoff = math.atan2(h,w)
degoff = 180*radoff/math.pi
poses = []
for do in [degoff,180-degoff,180+degoff,360-degoff]:
    with td.Pen((0,0)) as t:
        t.setheading(do)
        t.penup()
        t.forward(bc_radius+sc_radius+hr/2)
        pos = t.pos()
        poses.append(pos)
        t.pendown()
    td.rect(pos,wr+1,hr+1,90+do,colors='black',fill=False)

td.line2((w/2,h/2),(-w/2,-h/2),colors='white')
td.line2((-w/2,h/2),(w/2,-h/2),colors='white')

blue_degoff = 180-degoff
red_degoff = 360-degoff
td.circle((0,0),bc_radius,blue_degoff,180,colors='blue')
td.circle((-sc_radius*math.cos(radoff),sc_radius*math.sin(radoff)),
            sc_radius,blue_degoff,colors='red')
td.circle((0,0),bc_radius,red_degoff,180,colors='red')
td.circle((sc_radius*math.cos(radoff),-sc_radius*math.sin(radoff)),
            sc_radius,red_degoff,colors='blue')

ur,ul,dl,dr=poses
w1 = (bc_radius+sc_radius+gr)*math.cos(radoff)
w3 = (bc_radius+sc_radius+2*br+2*gr+gr)*math.cos(radoff)
h1 = (bc_radius+sc_radius+gr)*math.sin(radoff)
h3 = (bc_radius+sc_radius+2*br+2*gr+gr)*math.sin(radoff)

do = 90+degoff
td.rect((w1,h1),wr,br,do,colors='black')
td.rect((w3,h3),wr,br,do,colors='black')
td.rect(ur,hr,gr,degoff,colors='white')
td.rect(ur,wr,br,do,colors='black')
td.rect(ur,wr+1,hr+1,do,colors='white',fill=False)

do = 270-degoff
td.rect((-w1,h1),wr,br,do,colors='black')
td.rect(ul,wr,br,do,colors='black')
td.rect((-w3,h3),wr,br,do,colors='black')
td.rect(ul,wr+1,hr+1,do,colors='white',fill=False)

do = 270+degoff
td.rect((-w1,-h1),wr,br,do,colors='black')
td.rect(dl,wr,br,do,colors='black')
td.rect((-w3,-h3),wr,br,do,colors='black')
td.rect(dl,br,gr,180+degoff,colors='white')
td.rect(dl,wr+1,hr+1,do,colors='white',fill=False)

do = 90-degoff
td.rect((w1,-h1),wr,br,do,colors='black')
td.rect((w3,-h3),wr,br,do,colors='black')
td.rect(dr,wr,br,do,colors='black')
td.rect(dr,hr,gr,180-degoff,colors='white')
td.rect(dr,wr+1,hr+1,do,colors='white',fill=False)

td.show()
