a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))
d = b * b - 4 * a * c
if d > 0:
    e = (-b + (d)**0.5) / (2 * a)
    f = (-b - (d)**0.5) / (2 * a)
    print(f"Roots are real and different: {e} and {f}")
elif d == 0:
    e = -b / (2 * a)
    print(f"Root is real and the same: {e}")
else:
    print("Roots are complex")

