from math import atan2
from dearpygui import core, simple
import star

HEIGHT = 500
# GUIDE = True
GUIDE = False
TITLE = 'America National Flag'

guide_color = [0, 0, 0, 255]
blue_color = [0, 0, 255, 255]
red_color = [255, 0, 0, 255]
white_color = [255, 255, 255, 255]

win_id = 'flag'
draw_id = 'frame'

height = HEIGHT
width = int(height * 1.9)

htile_len = height / 13
star_rect_width = width * 2 / 5
star_rect_height = height * 7 / 13


def draw_guide_line(start, end):
    if GUIDE:
        core.draw_line(draw_id, start, end, guide_color, 1)


def draw_guide_rect(pmin, pmax):
    if GUIDE:
        core.draw_rectangle(draw_id, pmin, pmax, guide_color)


def draw_guide_circle(center_point, radius):
    if GUIDE:
        core.draw_circle(draw_id, center_point, radius, color=guide_color)


def draw_guide_poly(nodelist):
    draw_guide_line(nodelist[0], nodelist[1])
    draw_guide_line(nodelist[1], nodelist[2])
    draw_guide_line(nodelist[2], nodelist[3])
    draw_guide_line(nodelist[3], nodelist[4])
    draw_guide_line(nodelist[4], nodelist[0])


with simple.window(win_id):
    core.add_drawing(draw_id, width=width, height=height)

core.draw_rectangle(draw_id, [0, 0], [width, height], white_color)
core.draw_rectangle(draw_id, [0, 0], [star_rect_width, star_rect_height],
                    blue_color,
                    fill=blue_color)

for i in range(0, 7):
    # draw_guide_line([star_rect_width,i*htile_len],[width,i*htile_len])
    color = white_color if i % 2 else red_color
    core.draw_rectangle(draw_id, [star_rect_width, i * htile_len],
                        [width, (i + 1) * htile_len],
                        color,
                        fill=color)

for i in range(7, 13):
    color = white_color if i % 2 else red_color
    core.draw_rectangle(draw_id, [0, i * htile_len],
                        [width, (i + 1) * htile_len],
                        color,
                        fill=color)

# spad_width = 1/3*stile_width , spad_width * 2 + stile_width *11 = star_rect_width
# spad_height = 1/3*stile_height ,spad_height * 2 + stile_height *9 = star_rect_height
stile_width = star_rect_width * 3 / 35
spad_width = star_rect_width * 1 / 35
stile_height = star_rect_height * 3 / 29
spad_height = star_rect_height * 1 / 29

for i in range(11):
    for j in range(9):
        if (i + j) % 2 == 0:
            center = (spad_width + (i + 0.5) * stile_width,
                      spad_height + (j + 0.5) * stile_height)
            radius = stile_height / 2
            nodelist = star.draw_star(draw_id, center, radius,
                                      atan2(-radius,
                                            0), white_color, white_color)
            draw_guide_circle(center, radius)
            draw_guide_poly(nodelist)

for i in range(0, 10):
    draw_guide_line(
        [spad_width, spad_height + i * stile_height],
        [star_rect_width - spad_width, spad_height + i * stile_height])

for i in range(0, 12):
    draw_guide_line(
        [spad_width + i * stile_width, spad_height],
        [spad_width + i * stile_width, star_rect_height - spad_height])

for i in range(1, 8):
    draw_guide_line([star_rect_width, i * htile_len], [width, i * htile_len])

for i in range(8, 13):
    draw_guide_line([0, i * htile_len], [width, i * htile_len])

draw_guide_rect([0, 0], [star_rect_width, star_rect_height])

core.set_main_window_title(TITLE)
core.start_dearpygui(primary_window=win_id)
