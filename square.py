def area(a):
    if a <= 0:
        raise ValueError("Side length must be greater than zero")
    return a * a

def perimeter(a):
    if a <= 0:
        raise ValueError("Side length must be greater than zero")
    return 4 * a
