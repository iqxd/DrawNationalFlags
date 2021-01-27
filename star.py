from math import sin,cos,pi
from dearpygui import core

def draw_star(drawing_id,center,radius,x_axis_offset_radian,color,fill):
    nodelist=[]
    x,y=center
    rs = x_axis_offset_radian
    for i in range(5):
        nodelist.append((x+cos(rs+i*pi*0.4)*radius,y+sin(rs+i*pi*0.4)*radius))
    
    n1,n2,n3,n4,n5 = nodelist
    core.draw_triangle(drawing_id,center,n1,n3,color,fill=color)
    core.draw_triangle(drawing_id,center,n3,n5,color,fill=color)
    core.draw_triangle(drawing_id,center,n5,n2,color,fill=color)
    core.draw_triangle(drawing_id,center,n2,n4,color,fill=color)
    core.draw_triangle(drawing_id,center,n4,n1,color,fill=color)
    return nodelist

