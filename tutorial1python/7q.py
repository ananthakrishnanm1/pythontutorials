a = float(input("Enter x-coordinate: "))
b = float(input("Enter y-coordinate: "))
if a > 0 and b > 0:
    print("Point is in Quadrant I")
elif a < 0 and b > 0:
    print("Point is in Quadrant II")
elif a < 0 and b < 0:
    print("Point is in Quadrant III")
elif a > 0 and b < 0:
    print("Point is in Quadrant IV")
else:
    print("Point is on an axis")

