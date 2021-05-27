
def cylinder_area(r, h, pi = 3.14):
    base_area = pi * r**2
    side_area = 2 * pi * r * h
    total_area = base_area * 2 + side_area
    return total_area

print(cylinder_area(5,2))


def cone_area(r, l, pi = 3.14):
    base_area = pi * r**2
    side_area = pi * r * l
    total_area = base_area + side_area
    return total_area

print(cone_area(5,2))

def sphere_area(r, pi = 3.14):
    area = 4 * pi * r**2
    return area

print(sphere_area(5))