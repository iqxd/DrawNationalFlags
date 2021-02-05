from math import sin,cos,atan2,pi
from dearpygui import core
from dearpygui import simple
import star

# GUIDE = False
GUIDE = True
HEIGHT = 1000

guide_color= [0, 0, 0, 255]
red_color = [255, 0, 0, 255]
yellow_color = [255, 255, 0, 255]


core.set_main_window_title('National Flag')
height = HEIGHT 
width = int(height * 1.5)
with simple.window('flag'):
    core.add_drawing('drawing',width=width,height=height)

def draw_hline(start_point,end_point):
    if GUIDE:
        core.draw_line('drawing',start_point,end_point,guide_color,1)

def draw_hcircle(center_point,radius):
    if GUIDE:
        core.draw_circle('drawing',center_point,radius,color=guide_color)

core.draw_rectangle('drawing',[0,0],[width,height],color=red_color,fill=red_color)

tlen = height/2/10

main_center = (tlen*5,tlen*5)
s1_center = (tlen*10,tlen*2)
s2_center = (tlen*12,tlen*4)
s3_center = (tlen*12,tlen*7)
s4_center = (tlen*10,tlen*9)

n1 = main_center[0], main_center[1]-tlen*3
n2 = main_center[0]-cos(pi*0.1)*tlen*3 , main_center[1]-sin(pi*0.1)*tlen*3
n3 = main_center[0]-cos(pi*54/180)*tlen*3,main_center[1]+sin(pi*54/180)*tlen*3
n4 = main_center[0]+cos(pi*54/180)*tlen*3,main_center[1]+sin(pi*54/180)*tlen*3
n5 = main_center[0]+cos(pi*0.1)*tlen*3 , main_center[1]-sin(pi*0.1)*tlen*3

main_nlist = [n1,n2,n3,n4,n5]

def draw_hpoly(nlist):
    draw_hline(nlist[0],nlist[1])
    draw_hline(nlist[1],nlist[2])
    draw_hline(nlist[2],nlist[3])
    draw_hline(nlist[3],nlist[4])
    draw_hline(nlist[4],nlist[0])

def draw_star(center,nlist):
    n1,n2,n3,n4,n5 = nlist
    core.draw_triangle('drawing',center,n1,n3,yellow_color,fill=yellow_color)
    core.draw_triangle('drawing',center,n3,n5,yellow_color,fill=yellow_color)
    core.draw_triangle('drawing',center,n5,n2,yellow_color,fill=yellow_color)
    core.draw_triangle('drawing',center,n2,n4,yellow_color,fill=yellow_color)
    core.draw_triangle('drawing',center,n4,n1,yellow_color,fill=yellow_color)

# draw_star(main_center,main_nlist)
main_nodelist = star.draw_star('drawing',main_center,3*tlen,atan2(-3*tlen,0),yellow_color,yellow_color)
draw_hpoly(main_nodelist)

for s in (s1_center,s2_center,s3_center,s4_center):
    rs = atan2(main_center[1]-s[1],main_center[0]-s[0])
    # s_nlist = []
    # for i in range(5):
    #     s_nlist.append((s[0] + cos(rs+i*pi*0.4)*tlen, s[1] + sin(rs+i*pi*0.4)*tlen))
    # draw_star(s,s_nlist)
    nodelist = star.draw_star('drawing',s,tlen,rs,yellow_color,yellow_color)
    draw_hpoly(nodelist)

for i in range(11):
    draw_hline([0,tlen*i],[width/2,tlen*i])
for j in range(16):
    draw_hline([tlen*j,0],[tlen*j,height/2])

draw_hline([width/2,height/2],[width/2,height])
draw_hline([width/2,height/2],[width,height/2])

draw_hcircle(main_center,tlen*3)
draw_hcircle(s1_center,tlen)
draw_hcircle(s2_center,tlen)
draw_hcircle(s3_center,tlen)
draw_hcircle(s4_center,tlen)

draw_hline(main_center,s1_center)
draw_hline(main_center,s2_center)
draw_hline(main_center,s3_center)
draw_hline(main_center,s4_center)

core.start_dearpygui(primary_window='flag')
