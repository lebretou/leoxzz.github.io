import svgwrite
import math
import random
from svgwrite import cm, mm

RATIOS = [0.26, 0.34, 0.42, 0.5, 0.58, 0.66, 0.74, 0.82]


def positions(name, ratio):
    # draw canvas
    img = svgwrite.Drawing(filename=name, size = (12*cm, 6*cm))
    
    # draw axes
    img.add(img.line(start=(3*cm,3*cm), end=(9*cm,3*cm), stroke='black', stroke_width=2))
    img.add(img.line(start=(3*cm,2.8*cm), end=(3*cm,3.2*cm), stroke='black', stroke_width=4))
    img.add(img.line(start=(9*cm,2.8*cm), end=(9*cm,3.2*cm), stroke='black', stroke_width=4))
    img.add(img.text('0', insert=(2.85*cm, 3.8*cm)))
    img.add(img.text('100', insert=(8.65*cm, 3.8*cm)))

    draw_points(img, ratio)

    img.save()

def draw_points(img, ratio):
    test_num, base_num = generate_integers(ratio)

    scaled_test_len = (test_num / 100.0) * 6.0
    scaled_base_len = (base_num / 100.0) * 6.0

    # draw points
    img.add(img.circle(center=((3+scaled_base_len)*cm, 2.5*cm),r=0.1*cm, fill='black'))
    img.add(img.circle(center=((3+scaled_test_len)*cm, 2.5*cm),r=0.1*cm, fill='black'))

    # add markers
    img.add(img.text('A', insert=((2.85+scaled_base_len)*cm, 2.2*cm)))
    img.add(img.text('B', insert=((2.85+scaled_test_len)*cm, 2.2*cm)))

def generate_integers(x):
    a = random.randint(1, 99)  # generate a random integer between 1 and 99
    b = a * x  # compute b as a times x
    while b >= 100:  # make sure b is less than 100
        a = random.randint(1, 99)
        b = a * x

    return a, b


if __name__ == '__main__':
    # index = 0

    # for ratio in RATIOS:
    #     positions(('position_aligned_' + str(index) + '.svg'), ratio)
    #     index += 1
    positions("example.svg", 0.5)