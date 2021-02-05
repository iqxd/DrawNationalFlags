import turtledraw as td
import math
td.set_turtlecfg(False)
td.set_filling(True)
td.set_animation(True)

HEIGHT = 600
h = HEIGHT
w = int(h * 1.9)
center = (0, 0)
wa = w/2
ha = h/2
center_a = (-wa/2,ha/2)
wc = ha/10
center_m = (-wa+5*wc,5*wc)
radius_m = 3*wc
center_s1 =(-wa+10*wc,ha-2*wc)
center_s2 =(-wa+12*wc,ha-4*wc)
center_s3 =(-wa+12*wc,ha-7*wc)
center_s4 =(-wa+10*wc,ha-9*wc)
radius_s = wc

td.set_window('National Flag', width=w, height=h, bg='gray')

td.rect(center, w, h, colors='red')

# guide line
td.grid(center_a,wa,ha,10,15,color='black')
td.circle(center_m,radius_m+1,colors='black',fill=False)
for c in [center_s1,center_s2,center_s3,center_s4]:
    td.circle(c,radius_s+1,colors='black',fill=False)
    td.line(center_m,c,color='black')

td.grid(center_a,wa,ha,10,15,color='red')

for c in [center_s1,center_s2,center_s3,center_s4]:
    td.line(center_m,c,color='red')
    relative_rad = math.atan2(c[1]-center_m[1],c[0]-center_m[0])
    relative_deg = 180*relative_rad/math.pi 
    td.star(c,relative_deg+180,radius_s,colors='yellow')
    td.circle(c,radius_s+1,colors='red',fill=False) 

td.star(center_m,90,radius_m,colors='yellow')
td.circle(center_m,radius_m+1,colors='red',fill=False) 

td.show()
