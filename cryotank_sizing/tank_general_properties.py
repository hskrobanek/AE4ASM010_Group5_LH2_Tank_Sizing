import numpy as np

def get_tank_volume(radius:float, length:float):
    '''
        Assumes V = pi*R^2*L + 4/3 pi*R^2*H with H = 3/4 R --> V = piR^2(L+R)
    '''
    return np.pi*radius**2*(length + radius)


def tank_height(max_radius:float, min_radius:float, max_length:float, step:int):
    '''
    Calculates the maximum tank height at each length increment in the specified fuselage section with properties:
    max_radius, min_radius, max_length with a specified number of slices (step).

    Assumes a linear change in fuselage profile.
    '''

    length_increment = max_length/step
    height = np.zeros(step)
    slope = (max_radius-min_radius)/max_length

    for i in range(step):
        height[i] = max_radius - slope*length_increment*i
    return height


