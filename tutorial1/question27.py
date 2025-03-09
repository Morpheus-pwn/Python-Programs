import cmath

def quadratic_roots(a, b, c):
    delta = (b**2) - 4*(a*c)

    if delta >= 0:
        x1 = (-b - delta**0.5) / (2*a)
        x2 = (-b + delta**0.5) / (2*a)
        return x1, x2
    else:
        x1 = (-b - cmath.sqrt(delta)) / (2 * a)
        x2 = (-b + cmath.sqrt(delta)) / (2 * a)
        return x1, x2

a = float(input("Enter the coefficient a: "))
b = float(input("Enter the coefficient b: "))
c = float(input("Enter the coefficient c: "))

root1, root2 = quadratic_roots(a, b, c)
print("The roots of the quadratic equation are:", root1, "and", root2)
