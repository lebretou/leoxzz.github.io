import svgwrite
import math
import random
from math import sin, cos
from svgwrite import cm, mm

RATIOS = [0.26, 0.34, 0.42, 0.5, 0.58, 0.66, 0.74, 0.82]
CENTER = (226, 113)
RADIUS = 100

def create_sector(img, fill, start_angle, angle):

    # Create a circular sector
    center = CENTER  # Center of the circle
    radius = RADIUS # Radius of the circle
    start_angle = start_angle # Starting angle of the sector
    angle = angle # Angle of the sector
    end_angle = start_angle + angle  # Ending angle of the sector
    start_x = center[0] + radius * math.cos(math.radians(start_angle))
    start_y = center[1] + radius * math.sin(math.radians(start_angle))
    end_x = center[0] + radius * math.cos(math.radians(end_angle))
    end_y = center[1] + radius * math.sin(math.radians(end_angle))
    large_arc_flag = 1 if angle > 180 else 0
    path_data = f'M{center[0]},{center[1]} L{start_x},{start_y} A{radius},{radius} 0 {large_arc_flag},1 {end_x},{end_y} Z'
    path = img.path(d=path_data, fill=fill, stroke='black', stroke_width=3)

    img.add(path)

def piechart(name, ratio):
    # draw canvas
    img = svgwrite.Drawing(filename=name, size = (12*cm, 6*cm))

    # generate patterns 
    pattern_1 = img.pattern(id='pattern-1', patternUnits='userSpaceOnUse',
                                        size=(10,10), patternTransform="rotate(45 0 0)")
    pattern_1.add(img.line(start=(0, 0), end=(0, 10), stroke='black', stroke_width=3))

    pattern_2 = img.pattern(id='pattern-2', patternUnits='userSpaceOnUse',
                                        size=(13,13), patternTransform="rotate(-45 0 0)")
    pattern_2.add(img.circle(center=(5,5), r=5, stroke='none', fill='black'))

    # generate angles
    nums = generate_angles(ratio)

    mark = 0
    start_angle = random.randint(0, 360)
    for num in nums:
        if num == nums[0] and mark < 2:
            create_sector(img, 'url(#pattern-1)',start_angle, num)
            start_angle += num
            mark += 1
            continue

        if num == nums[1] and mark < 2:
            create_sector(img, 'url(#pattern-2)',start_angle, num)
            start_angle += num
            mark += 1
            continue

        create_sector(img, 'white',start_angle, num)
        start_angle += num
    
    img.add(pattern_1)
    img.add(pattern_2)
    img.save()



def generate_angles(ratio):
    smaller_num = (100.0 * ratio) / (ratio + 1.0)
    larger_num = 100.0 / (ratio + 1.0)

    smaller_num = smaller_num * 360 / 100.0
    larger_num = larger_num * 360 / 100.0

    coin_flip = random.randint(0, 1)
    if coin_flip == 0:
        tmp = smaller_num
        smaller_num = larger_num
        larger_num = tmp


    return smaller_num, larger_num

if __name__ == '__main__':
    # index = 0

    # for ratio in RATIOS:
    #     piechart(('piechart_' + str(index) + '.svg'), ratio)
    #     index += 1
    piechart("example.svg", 0.7)