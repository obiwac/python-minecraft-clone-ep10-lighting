transparent = False
is_cube = True

vertex_positions = [
    [0.5, 0.5, 0.5, 0.5, -0.5, 0.5, 0.5, -0.5, -0.5, 0.5, 0.5, -0.5],  # right
    [-0.5, 0.5, -0.5, -0.5, -0.5, -0.5, -0.5, -0.5, 0.5, -0.5, 0.5, 0.5],  # left
    [0.5, 0.5, 0.5, 0.5, 0.5, -0.5, -0.5, 0.5, -0.5, -0.5, 0.5, 0.5],  # top
    [-0.5, -0.5, 0.5, -0.5, -0.5, -0.5, 0.5, -0.5, -0.5, 0.5, -0.5, 0.5],  # bottom
    [-0.5, 0.5, 0.5, -0.5, -0.5, 0.5, 0.5, -0.5, 0.5, 0.5, 0.5, 0.5],  # front
    [0.5, 0.5, -0.5, 0.5, -0.5, -0.5, -0.5, -0.5, -0.5, -0.5, 0.5, -0.5],  # back
]

tex_coords = [
    [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0],
    [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0],
    [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0],
    [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0],
    [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0],
    [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0],
]

shading_values = [
    [0.6, 0.6, 0.6, 0.6],
    [0.6, 0.6, 0.6, 0.6],
    [1.0, 1.0, 1.0, 1.0],
    [0.4, 0.4, 0.4, 0.4],
    [0.8, 0.8, 0.8, 0.8],
    [0.8, 0.8, 0.8, 0.8],
]

import options

max_light_level = 15


def get_face_shading_values(light_level, face_number):  # very inefficient way of doing it :/
    if not options.LIGHTING:
        return shading_values[face_number]
    s = (shading_values[face_number][0] *
         (light_level + 1 + options.BRIGHTNESS * 4) / (max_light_level + 1))  # Minecraft's shading values doesnt seem
    # to be linear though
    t = [s, s, s, s]
    return t
