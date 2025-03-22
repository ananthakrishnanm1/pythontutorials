a = int(input("Enter a positive integer: "))
b = 0
for i in range(2, a + 1, 2):
    b += i ** 3
print(f"Sum of cubes of even numbers: {b}")

