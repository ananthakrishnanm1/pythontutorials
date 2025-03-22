a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))
if a * a + b * b == c * c or a * a + c * c == b * b or b * b + c * c == a * a:
    print("The triangle is a right-angled triangle")
else:
    print("The triangle is not a right-angled triangle")

