import math

def area(r):
    if r <= 0:
        raise ValueError("Radius must be greater than zero")
    return math.pi * r * r

def perimeter(r):
    if r <= 0:
        raise ValueError("Radius must be greater than zero")
    return 2 * math.pi * r
