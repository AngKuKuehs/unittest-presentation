
def is_valid_triangle(a,b,c):
    return a + b > c and b + c > a and c + a > b

def type_of_triangle(a,b,c):
    if not is_valid_triangle(a, b, c):
        raise ValueError

    if a==b and b==c:
        return "Equilateral"
    elif a==b or b==c or a==c:
        return "Isosceles"
    else:
        return "Scalene"
