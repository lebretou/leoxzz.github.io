import svgwrite
import math
import random
from svgwrite import cm, mm

RATIOS = [0.26, 0.34, 0.42, 0.5, 0.58, 0.66, 0.74, 0.82]
BASE_RADIUS = 1.5


def areas(name, ratio):
    # draw canvas
    img = svgwrite.Drawing(filename=name, size = (12*cm, 6*cm))

    # define centers and radii 
    circle_a_center = (3, 3)
    circle_b_center = (9, 3)
    circle_a_radius = BASE_RADIUS
    circle_b_radius = circle_a_radius/math.sqrt(ratio)

    pattern = img.pattern(id='pattern', patternUnits='userSpaceOnUse',
                                        size=(10,10), patternTransform="rotate(45 0 0)")
    pattern.add(img.line(start=(0, 0), end=(0, 10), stroke='black', stroke_width=3))


    # 50% chance to swap the position of line a and line b
    coin_flip = random.randint(0, 1)
    if (coin_flip == 0):
        tmp_c = circle_a_center
        circle_a_center = circle_b_center
        circle_b_center = tmp_c 

    # draw circles
    circle_a = img.circle(center = (circle_a_center[0] * cm, circle_a_center[1] * cm), r=circle_a_radius * cm, stroke='black', stroke_width=3, fill='url(#pattern)')
    circle_b = img.circle(center = (circle_b_center[0] * cm, circle_b_center[1] * cm), r=circle_b_radius * cm, stroke='black', stroke_width=3, fill='url(#pattern)')

    # add markers
    marker_a = img.text('A', insert=(5.8 * 37.6, 5.8 * 37.6))
    marker_b = img.text('B', insert=(11.8 * 37.6, 5.8 * 37.6))

    img.add(pattern)
    img.add(circle_a)
    img.add(circle_b)
    img.add(marker_a)
    img.add(marker_b)
    img.save()
    

if __name__ == '__main__':
    areas("example.svg", 0.4)


   
       
       
       