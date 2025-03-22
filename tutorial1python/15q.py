for a in range(2, 1000):
    b = 2
    while b * b <= a:
        if a % b == 0:
            break
        b += 1
    else:
        print(a, end=" ")
print()

