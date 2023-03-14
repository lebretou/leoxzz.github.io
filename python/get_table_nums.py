import random
RATIOS = [0.26, 0.34, 0.42, 0.5, 0.58, 0.66, 0.74, 0.82]

def generate_pairs(ratios):
    pairs = []
    for i in range(len(ratios)):
        larger_num = random.uniform(0, 100)
        smaller_num = larger_num * ratios[i]
        larger_num = round(larger_num, 1)
        smaller_num = round(smaller_num, 1)

        coin_flip = random.randint(0, 1)
        if coin_flip == 0:
            tmp = larger_num
            larger_num = smaller_num
            smaller_num = tmp
        pairs.append([larger_num, smaller_num])

    return pairs

print(generate_pairs(RATIOS))
