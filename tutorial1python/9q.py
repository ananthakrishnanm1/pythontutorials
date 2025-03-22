a = int(input("Enter a number: "))
b = 2
while b * b <= a:
    if a % b == 0:
        print(f"{a} is not a prime number")
        break
    b += 1
else:
    print(f"{a} is a prime number")

