"""
Generates sand.xml bodies for the gravel environment.
The sand is generated in a circular dump zone with radius 3, and then
randomly sampled from this zone.
"""
import random
import numpy as np

def generate_random_rgba():
    # generate random gray shade
    grayshade = random.uniform(0.0, 0.4)
    # generate random moss shade
    
    return [grayshade, grayshade , grayshade, 1.0]


def generate_sphere_xml(name, pos):
    rgba = generate_random_rgba()
    rgba_str = ' '.join(map(str, rgba))
    return f'<body name="{name}" pos="{pos}">\n' \
    f' <joint name="ball\_joint{name}" type="free" damping="0.9" stiffness="1.2" /> \n' \
    f'<geom name="ball\_geom{name}" size="0.04" rgba="{rgba_str}" type="sphere" density="100" friction="0.5" euler="0 10 0"/>\n' \
    '</body>'


# Define the size of the square
square_size = 4

dump_zones = 2
positions = [[0,0], [1,1]]
# location of dump zones 0,0 and 1,1

sand_per_zone = 200

sand_xml = ""

for j in range(sand_per_zone):
    # for each dump zone, generate sand
        # randomly sample from a circular dump zone with radius 3
        length = random.uniform(0, 1)
        angle = random.uniform(0, 2 * 3.14159)
        
        x = np.sqrt(length) * np.cos(angle)
        y = np.sqrt(length) * np.sin(angle)

        pos = f"{x} {y} 0.001"
        name = f"sand_{x}_{y}"

        sand_xml += generate_sphere_xml(name, pos) + '\n'



with open("sand.xml", "w") as file:
    file.write(sand_xml)

print("done")

