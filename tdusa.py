import turtledraw as td

td.set_turtle(True)
td.set_filling(True)
td.set_animation(True)

HEIGHT = 400
h=height = HEIGHT
w=width = int(height * 1.9)

hs = strip_height = height/13
wa = star_area_width = width * 2 / 5
ha = star_area_height = height * 7 / 13
wc = star_cell_width = star_area_width * 3 / 35
hc = star_cell_height = star_area_height * 3 / 29
wp = star_padding_width = star_area_width * 1 / 35
hp = star_padding_height = star_area_height * 1 / 29

td.set_window('National Flag',width=width,height=height,bg='black')

td.rect((-(w-wa)/2,(h-ha)/2),wa,ha,colors='blue')

for i in range(13):
    if i <7:
        center_x,ws = wa/2,w-wa
    else:
        center_x,ws = 0,w
    center_y = h/2-hs/2-hs*i
    strip_color = 'white' if i%2 else 'red'
    td.rect((center_x,center_y),ws,hs,strip_color)

for i in range(11):
    for j in range(9):
        if (i+j) % 2 == 0:
            rx,ry = (i+0.5)*wc,(j+0.5)*hc
            center = (-w/2+wp+rx,h/2-hp-ry)
            td.star(center,90,hc/2,colors='white')

td.show()


