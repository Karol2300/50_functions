
def cylinder_volume(r, h, pi = 3.14):
    volume = pi * r ** 2 * h
    return volume

print(cylinder_volume(5, 2))


def cone_volume(r, h, pi = 3.14):
    volume = (1 / 3) * pi * r ** 2 * h
    return volume

print(cone_volume(5,2))

def sphere_volume(r, pi = 3.14):
    volume = 4/3 * pi * r ** 2
    return volume

print(sphere_volume(5))