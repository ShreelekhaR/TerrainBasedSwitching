import random

def generate_random_rgba():
    # generate random cobblestone color
    # cobblestone colors are in range 0.4-0.6
    grayshade = random.uniform(0.4, 0.6)
    # generate random color for the moss
    # moss colors are in range 0.0-0.4
    moss = random.uniform(0.0, 0.4)

    return [grayshade, grayshade - moss, grayshade - moss, 1.0]

def generate_sphere_xml(name, pos):
    rgba = generate_random_rgba()
    rgba_str = ' '.join(map(str, rgba))
    return f'<geom name="{name}" pos="{pos}" size=".13" rgba="{rgba_str}"/>'



# Define the size of the square
square_size = 4

# Calculate the spacing between spheres
spacing = 0.4

# Calculate the number of spheres in each dimension
num_spheres_x = int(square_size / spacing) + 1
num_spheres_y = int(square_size / spacing) + 1

print(f"num_spheres_x: {num_spheres_x}")
print(f"num_spheres_y: {num_spheres_y}")

# Calculate the total size covered by spheres in each dimension
total_size_x = spacing * (num_spheres_x - 1)
total_size_y = spacing * (num_spheres_y - 1)

# Calculate the starting position to center the grid within the square
start_x = (square_size - total_size_x) / 2
start_y = (square_size - total_size_y) / 2

# Generate sphere XML for the grid
spheres_xml = ""
for i in range(num_spheres_x):
    for j in range(num_spheres_y):
        name = f"green_sphere_{i}_{j}"
        pos = f"{start_x + i * spacing} {start_y + j * spacing} 0.001"
        spheres_xml += generate_sphere_xml(name, pos) + '\n'

        # do same with negative first pos if not at origin
        if i != 0:
            name = f"green_sphere_{-i}_{j}"
            pos = f"{-start_x - i * spacing} {start_y + j * spacing} 0.001"
            spheres_xml += generate_sphere_xml(name, pos) + '\n'

        # do same with negative second pos if not at origin
        if j != 0:
            name = f"green_sphere_{i}_{-j}"
            pos = f"{start_x + i * spacing} {-start_y - j * spacing} 0.001"
            spheres_xml += generate_sphere_xml(name, pos) + '\n'

        # do same with negative both pos
        if i != 0 and j != 0:
            name = f"green_sphere_{-i}_{-j}"
            pos = f"{-start_x - i * spacing} {-start_y - j * spacing} 0.001"
            spheres_xml += generate_sphere_xml(name, pos) + '\n'


# print(spheres_xml)
# print to file
print("Writing to file...")
with open("green_spheres.xml", "w") as f:
    f.write(spheres_xml)
f.close()
# print to stdout


