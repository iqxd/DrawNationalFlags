import turtledraw as td
td.set_turtlecfg(False)
td.set_filling(True)
td.set_animation(True)

HEIGHT = 600
h = HEIGHT
w = int(h* 1.9)
hs   = h/13  # strip_height
wa   = w * 2 / 5 # star_area_width
ha  = h * 7 / 13 # star_area_height 
wc  = wa * 3 / 35 # star_cell_width 
hc  = ha * 3 / 29 # star_cell_height 
wp  = wa * 1 / 35 # star_padding_width 
hp  = ha * 1 / 29 # star_padding_height 
center_a = (-(w-wa)/2,(h-ha)/2)

td.set_window('National Flag',width=w,height=h,bg='gray')

td.rect(center_a,wa,ha,colors='blue')

for i in range(13):
    if i <7:
        center_x,ws = wa/2,w-wa
    else:
        center_x,ws = 0,w
    center_y = h/2-hs/2-hs*i
    strip_color = 'white' if i%2 else 'red'
    td.rect((center_x,center_y),ws,hs,strip_color)

td.grid(center_a,wa-2*wp,ha-2*hp,9,11,color='black')

for i in range(11):
    for j in range(9):
        if (i+j) % 2 == 0:
            rx,ry = (i+0.5)*wc,(j+0.5)*hc
            center = (-w/2+wp+rx,h/2-hp-ry)
            td.star(center,90,hc/2-1,colors='white')

td.grid(center_a,wa-2*wp,ha-2*hp,9,11,color='blue')

td.show()


