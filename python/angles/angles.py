import svgwrite
import math
import random
from math import sin, cos
from svgwrite import cm, mm

RATIOS = [0.26, 0.34, 0.42, 0.5, 0.58, 0.66, 0.74, 0.82]
BASE_ANGLE = 45

def angles(name, ratio):
    # draw canvas
    img = svgwrite.Drawing(filename=name, size = (12*cm, 6*cm))

    # create base angle lines
    baseline_a = img.line(start=(3*cm,3*cm), end=(6*cm,3*cm),stroke='black', stroke_width=3)
    baseline_b = img.line(start=(9*cm,3*cm), end=(12*cm,3*cm),stroke='black', stroke_width=3)

    # define angles and center
    angle_a = BASE_ANGLE
    angle_b = angle_a / ratio
    angle_a_center = (3, 3)
    angle_b_center = (9, 3)


    # 50% swap
    coin_flip = random.randint(0, 1)
    if coin_flip == 0:
        tmp = angle_a
        angle_a = angle_b
        angle_b = tmp

    angle_line_a_end = angle_line(angle_a, angle_a_center)
    angle_line_b_end = angle_line(angle_b, angle_b_center)

    angle_line_a = img.line(start=(angle_a_center[0]*cm, angle_a_center[1]*cm), end=(angle_line_a_end[0]*cm, angle_line_a_end[1]*cm), stroke='black', stroke_width=3)
    angle_line_b = img.line(start=(angle_b_center[0]*cm, angle_b_center[1]*cm), end=(angle_line_b_end[0]*cm, angle_line_b_end[1]*cm), stroke='black', stroke_width=3)

    # rotate the angles randomly 
    rotate_angle_a = random.randint(-90, 90)
    baseline_a.rotate(rotate_angle_a, center=(3 * 37.6,3 * 37.6))
    angle_line_a.rotate(rotate_angle_a, center=(3 * 37.6,3 * 37.6))

    rotate_angle_b = random.randint(-90, 90)
    baseline_b.rotate(rotate_angle_b, center=(9 * 37.6,3 * 37.6))
    angle_line_b.rotate(rotate_angle_b, center=(9 * 37.6,3 * 37.6))

    # add markers
    marker_a = img.text('A', insert=(5.8 * 37.6, 5.8 * 37.6))
    marker_b = img.text('B', insert=(11.8 * 37.6, 5.8 * 37.6))

    img.add(baseline_a)
    img.add(baseline_b)
    img.add(angle_line_a)
    img.add(angle_line_b)
    img.add(marker_a)
    img.add(marker_b)
    img.save()

def angle_line(angle, center):
    end_x = center[0] + 2.6 * cos(math.radians(angle))
    start_x = center[1] - 2.6 * sin(math.radians(angle))

    return (end_x, start_x)


if __name__ == '__main__':
    # index = 0

    # for ratio in RATIOS:
    #     angles(('angles_' + str(index) + '.svg'), ratio)
    #     index += 1

    angles("example.svg", 0.3)