a = int(input("Enter a number: "))
b = 2
while a > 1:
    if a % b == 0:
        print(b, end=" ")
        a //= b
    else:
        b += 1
print()

