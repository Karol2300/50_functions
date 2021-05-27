def rectangle_perimeter(a ,b):
    return 2 * a + 2 * b
print(rectangle_perimeter(2,3))

def rectangle_area(a ,b):
    return a * b
print(rectangle_area(1,2))

def square_perimeter(a):
    return 4 * a
print(square_perimeter(2))

def square_area(a):
    return a**2
print(square_area(2))

def paralellogram_perimeter(a ,b):
    return 2*(a+b)
print(paralellogram_perimeter(2,3))

def paralellogram_area(a ,h):
    return a * h
print(paralellogram_area(2,3))

def diamond_perimeter(a):
    return 4 * a
print(diamond_perimeter(2))

def diamond_area(a, h):
    return a * h
print(diamond_area(2,3))

def trapeze_area(a, b, h):
    return ((a +b) * h) / 2
print(trapeze_area(2,3,4))

def pitagoras_theorem_check(a, b, c):
    if a**2 + b**2 == c**2:
        return True
    else:
        return False
print(pitagoras_theorem_check(3, 4, 5))

def circle_perimeter(r, pi = 3.14):
    return 2 * pi * r
print(circle_perimeter(3))

def circle_area(r, pi = 3.14):
    return pi * r**2
print(circle_area(3))