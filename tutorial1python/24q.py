for a in range(100, 1000):
    b = sum(int(digit) for digit in str(a))
    if b % 9 == 0:
        print(a, end=" ")
print()

