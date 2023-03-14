import os

def get_svg_paths(root_path):
    svg_paths = []
    for dirpath, dirnames, filenames in os.walk(root_path):
        for filename in filenames:
            if filename.startswith('example'):
                svg_paths.append('../../python'+os.path.join(dirpath, filename)[1:])
    return svg_paths

root_path = "./"

svg_paths = get_svg_paths(root_path)

with open('example_paths.txt', "w") as file:
    for path in svg_paths:
        file.write(path + "\n")

file.close()