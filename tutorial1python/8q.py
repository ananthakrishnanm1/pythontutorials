a = int(input("Enter a number: "))
b = 0
while a > 0:
    b += a % 10
    a //= 10
print(f"Sum of digits: {b}")

