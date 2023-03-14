import svgwrite
import random
from svgwrite import cm, mm


MAX_LENGTH = 6
RATIOS = [0.26, 0.34, 0.42, 0.5, 0.58, 0.66, 0.74, 0.82]
BASE_LENGTH = 1.5

def lines(name, ratio):
    # create canvas
    img = svgwrite.Drawing(filename=name, size = (12*cm, 6*cm))

    # define loc for lines
    line_a_start, line_a_end = (3, 2.25), (3, 3.75)
    line_b_start, line_b_end = line_coordinates(BASE_LENGTH / ratio, (9, 3))
    line_a_center = (3,3)
    line_b_center = (9,3)


    # 50% chance to swap the position of line a and line b
    coin_flip = random.randint(0, 1)
    if (coin_flip == 0):
        tmp_s, tmp_e, tmp_c = line_a_start, line_a_end, line_a_center
        line_a_start, line_a_end, line_a_center = line_b_start, line_b_end, line_b_center
        line_b_start, line_b_end, line_b_center = tmp_s, tmp_e, tmp_c

    # draw and rotate line a
    line_a = img.line(start=(line_a_start[0]*cm, line_a_start[1]*cm), end=(line_a_end[0]*cm,line_a_end[1]*cm), stroke='black', stroke_width=4)
    rotate_angle_a = random.randint(-90, 90)
    line_a.rotate(rotate_angle_a, center=(line_a_center[0] * 37.6,line_a_center[1] * 37.6))

    # draw and rotate line b
    line_b = img.line(start=(line_b_start[0]*cm, line_b_start[1]*cm), end=(line_b_end[0]*cm,line_b_end[1]*cm), stroke='black', stroke_width=4)
    rotate_angle_b = random.randint(-90, 90)
    line_b.rotate(rotate_angle_b, center=(line_b_center[0] * 37.6,line_b_center[1] * 37.6))
    
    # add markers
    marker_a = img.text('A', insert=(5.8 * 37.6, 5.8 * 37.6))
    marker_b = img.text('B', insert=(11.8 * 37.6, 5.8 * 37.6))

    img.add(line_a)
    img.add(line_b)
    img.add(marker_a)
    img.add(marker_b)
    img.save()

# length and center in the unit of cm
def line_coordinates(length, center):
    half = length / 2.0
    start = (center[0], center[1] - half)
    end = (center[0], center[1] + half)
    return start, end



if __name__ == '__main__':
    
    # index = 0

    # for ratio in RATIOS:
    #     lines(('lines_' + str(index) + '.svg'), ratio)
    #     index += 1

    lines("example.svg", 0.5)
