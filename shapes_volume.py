
def walec_volume(r, h, pi = 3.14):
    volume = pi * r ** 2 * h
    return volume

print(walec_volume(5,2))


def stozek_volume(r, h, pi = 3.14):
    volume =1/3 * pi * r ** 2 * h
    return volume

print(stozek_volume(5,2))

def sphere_volume(r, pi = 3.14):
    volume = 4/3 * pi * r ** 2
    return volume

print(sphere_volume(5))