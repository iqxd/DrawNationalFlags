import turtledraw as td
import math
td.set_turtlecfg(True)
td.set_filling(True)
td.set_animation(True)

HEIGHT = 400
h = HEIGHT
wh_ratio = 2.0
w =  h*wh_ratio
diagonal = (w**2+h**2)**0.5
center = (0,0)

w_segs = 60
h_segs = 30
ws = w/w_segs
hs = h/h_segs

td.set_window('National Flag', width=w, height=h, bg='gray')

td.rect(center,w,h,colors='blue')

ds = math.sqrt((hs**2+ws**2)/2)
radoff = math.atan2(h,w)
ws_hy = ds / math.sin(radoff)
hs_hy = ds / math.cos(radoff)

td.line2((0,h/2),(0,-h/2),colors='black')
td.line2((-w/2,0),(w/2,0),colors='black')

upright = (w/2,h/2)
downleft = (-w/2,-h/2)
urw_p=[upright]
urh_p=[upright]
dlw_p=[downleft]
dlh_p=[downleft]

td.line2(upright,downleft,colors='black')
for i in range(1,4):
    urw = (upright[0]-ws_hy*i,upright[1])
    dlh = (downleft[0],downleft[1]+hs_hy*i)
    td.line2(urw,dlh,colors='black')
    urh = (upright[0],upright[1]-hs_hy*i)
    dlw = (downleft[0]+ws_hy*i,downleft[1])
    td.line2(urh,dlw,colors='black')
    urw_p.append(urw)
    urh_p.append(urh)
    dlw_p.append(dlw)
    dlh_p.append(dlh)

upleft = (-w/2,h/2)
downright = (w/2,-h/2)
ulw_p = [upleft]
ulh_p = [upleft]
drw_p = [downright]
drh_p = [downright]

td.line2(upleft,downright,colors='black')
for i in range(1,4):
    ulw =(upleft[0]+ws_hy*i,upleft[1])
    drh =(downright[0],downright[1]+hs_hy*i)
    td.line2(ulw,drh,colors='black')
    ulh =(upleft[0],upleft[1]-hs_hy*i)
    drw = (downright[0]-ws_hy*i,downright[1])
    td.line2(ulh,drw,colors='black')
    ulw_p.append(ulw)
    ulh_p.append(ulh)
    drw_p.append(drw)
    drh_p.append(drh)

td.poly(urw_p[2],urw_p[3],dlh_p[3],dlh_p[2],colors='white')
td.poly(dlh_p[0],dlh_p[2],(0,2*hs_hy),center,colors='white')
td.poly(urw_p[0],urw_p[2],(-2*ws_hy,0),center,colors='red')
td.poly(urh_p[2],urh_p[3],dlw_p[3],dlw_p[2],colors='white')
td.poly(urh_p[0],urh_p[2],(0,-2*hs_hy),center,colors= 'white')
td.poly(dlw_p[0],dlw_p[2],(2*ws_hy,0),center,colors='red')

td.poly(ulw_p[2],ulw_p[3],drh_p[3],drh_p[2],colors='white')
td.poly(ulw_p[0],ulw_p[2],(2*ws_hy,0),center,colors='white')
td.poly(drh_p[0],drh_p[2],(0,2*hs_hy),center,colors='red')
td.poly(ulh_p[2],ulh_p[3],drw_p[3],drw_p[2],colors='white')
td.poly(drw_p[0],drw_p[2],(-2*ws_hy,0),center,colors='white')
td.poly(ulh_p[0],ulh_p[2],(0,-2*hs_hy),center,colors= 'red')

td.rect((0,0),w,10*hs,colors='white')
td.rect((0,0),10*ws,h,colors='white')

td.rect((0,0),w,6*hs,colors='red')
td.rect((0,0),6*ws,h,colors='red')

td.show()
