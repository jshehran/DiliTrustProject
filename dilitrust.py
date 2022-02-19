# Python function to print whether given triangle is
# Equilateral - If all the sides are equal
# Isosceles - If any of two sides are equal
# Right Angled - If sum of square of two sides are equal to square of third side
# Nothing special
def trianglo(x,y,z):
    result = ""
    if x == y == z:
        result = "Equilateral"
    elif x == y or y == z or z == x:
        result = "Isosceles"
    elif ( x*x + y*y == z*z) or (y*y + z*z == x*x) or (z*z + x*x == y*y):
        result = "Right Angled"
    else:
        result = "nothing special"
    return result