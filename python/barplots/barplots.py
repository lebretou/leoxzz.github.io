import svgwrite
import math
import random
from math import sin, cos
from svgwrite import cm, mm

RATIOS = [0.26, 0.34, 0.42, 0.5, 0.58, 0.66, 0.74, 0.82]
BASE_NUM = 3
BIN_WIDTH = 1.2
SPACE = 0.4
STARTING_POINTS = [4.4, 7.2]


def barplots(name, ratio):
    # draw canvas
    img = svgwrite.Drawing(filename=name, size = (12*cm, 6*cm))

    # draw axes
    y_axis = img.line(start=(2.5*cm, 0.8*cm), end=(2.5*cm, 4.8*cm), stroke='black', stroke_width=3)
    x_axis = img.line(start=(2.6*cm, 4.8*cm), end=(10*cm, 4.8*cm), stroke='black',stroke_width=3)
    img.add(img.line(start=(2.2*cm, 4.8*cm),end=(2.54*cm,4.8*cm), stroke='black', stroke_width=3))
    img.add(img.line(start=(2.2*cm, 0.8*cm),end=(2.54*cm,0.8*cm), stroke='black', stroke_width=3))
    img.add(img.text('100', insert=(1.2*37.6, 1.0*37.6)))
    img.add(img.text('0', insert=(1.7*37.6, 5*37.6)))


    draw_bins(img, ratio)

    img.add(y_axis)
    img.add(x_axis)
    img.save()

def draw_bins(img, ratio):
    # generate the values for the bins
    nums = generate_random_numbers(ratio)
    markers = ['A', 'B']
    marker_i = 0

    pattern = img.pattern(id='pattern', patternUnits='userSpaceOnUse',
                                        size=(10,10), patternTransform="rotate(45 0 0)")
    pattern.add(img.line(start=(0, 0), end=(0, 10), stroke='black', stroke_width=3))

    pattern_2 = img.pattern(id='pattern-2', patternUnits='userSpaceOnUse',
                                        size=(13,13), patternTransform="rotate(-45 0 0)")
    pattern_2.add(img.circle(center=(5,5), r=5, stroke='none', fill='black'))


    i = 0
    for num in nums:
        scaled_value = (num / 100.0) * 4.0

        if num == nums[0]:
            img.add(img.rect(insert=(STARTING_POINTS[i] * cm, (4.8 - scaled_value) * cm),size=(BIN_WIDTH*cm, scaled_value*cm), stroke='black', stroke_width=3, fill='url(#pattern)'))
            img.add(img.text(markers[marker_i], insert=((STARTING_POINTS[i] + 0.4)*37.6, 5.5*37.6)))
            marker_i += 1
            i += 1
            continue

        if num == nums[1]:
            img.add(img.rect(insert=(STARTING_POINTS[i] * cm, (4.8 - scaled_value) * cm),size=(BIN_WIDTH*cm, scaled_value*cm), stroke='black', stroke_width=3, fill='url(#pattern-2)'))
            img.add(img.text(markers[marker_i], insert=((STARTING_POINTS[i] + 0.4)*37.6, 5.5*37.6)))
            marker_i += 1
            i += 1
            continue

        img.add(img.rect(insert=(STARTING_POINTS[i] * cm, (4.8 - scaled_value) * cm),size=(BIN_WIDTH*cm, scaled_value*cm), stroke='black', stroke_width=3, fill='white'))
        i += 1
    
    img.add(pattern_2)
    img.add(pattern)
    


def generate_random_numbers(ratio):
    smaller_num = (100.0 * ratio) / (ratio + 1.0)
    larger_num = 100.0 / (ratio + 1.0)


    coin_flip = random.randint(0, 1)
    if coin_flip == 0:
        tmp = smaller_num
        smaller_num = larger_num
        larger_num = tmp


    return [smaller_num, larger_num]

if __name__ == '__main__':
    # index = 0

    # for ratio in RATIOS:
    #     barplots(('barplots_' + str(index) + '.svg'), ratio)
    #     index += 1

    barplots("example.svg", 0.6)