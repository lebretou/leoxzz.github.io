import svgwrite
import math
import random
from math import sin, cos
from svgwrite import cm, mm

RATIOS = [0.26, 0.34, 0.42, 0.5, 0.58, 0.66, 0.74, 0.82]
BASE_CURVE = 0.3


def curves(name, ratio):
    # draw canvas
    img = svgwrite.Drawing(filename=name, size = (12*cm, 6*cm))

    # calculate points for the base curve
    b_start, b_end = (1.5*37.6, 3*37.6), (4.5*37.6, 3*37.6)
    b_cx1, b_cy1, b_cx2, b_cy2 = calculate_control(b_start, b_end, BASE_CURVE)

    # calculate for test curve
    t_start, t_end = (7.5*37.6, 3*37.6), (10.5*37.6, 3*37.6)
    t_cx1, t_cy1, t_cx2, t_cy2 = calculate_control(t_start, t_end, BASE_CURVE / ratio)

    base_curve = img.path(d=f"M {b_start[0]},{b_start[1]} C {b_cx1},{b_cy1} {b_cx2},{b_cy2} {b_end[0]},{b_end[1]}", stroke='black', stroke_width=3, fill='none')
    test_curve = img.path(d=f"M {t_start[0]},{t_start[1]} C {t_cx1},{t_cy1} {t_cx2},{t_cy2} {t_end[0]},{t_end[1]}", stroke='black', stroke_width=3, fill='none')

    # random rotation
    rotate_angle_a = random.randint(-90, 90)
    rotate_angle_b = random.randint(-90, 90)

    base_curve.rotate(rotate_angle_a, center=(3*37.6, 3*37.6))
    test_curve.rotate(rotate_angle_b, center=(9*37.6, 3*37.6))

    # add markers
    marker_a = img.text('A', insert=(5.8 * 37.6, 5.8 * 37.6))
    marker_b = img.text('B', insert=(11.8 * 37.6, 5.8 * 37.6))
    

    img.add(marker_a)
    img.add(marker_b)
    img.add(base_curve)
    img.add(test_curve)
    
    img.save()


def calculate_control(start, end, curvature):
    cx1 = start[0] + (end[0] - start[0]) / 2.0 - (end[1] - start[1]) * curvature
    cy1 = start[1] + (end[1] - start[1]) / 2.0 - (end[0] - start[0]) * curvature
    cx2 = end[0] - (end[0] - start[0]) / 2.0 - (end[1] - start[1]) * curvature
    cy2 = end[1] - (end[1] - start[1]) / 2.0 - (end[0] - start[0]) * curvature

    return cx1, cy1, cx2, cy2


if __name__ == '__main__':
    # index = 0

    # for ratio in RATIOS:
    #     curves(('curvatures_' + str(index) + '.svg'), ratio)
    #     index += 1
    curves("example.svg", 0.4)