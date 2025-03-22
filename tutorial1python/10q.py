n = int(input("Enter how many numbers: "))
sum_even = 0
for i in range(n):
    a = int(input(f"Enter number {i + 1}: "))
    if a % 2 == 0:
        sum_even += a
print(f"Sum of even numbers: {sum_even}")

