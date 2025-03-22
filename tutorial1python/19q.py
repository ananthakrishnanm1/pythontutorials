n = int(input("Enter the number of elements: "))
even_count = 0
odd_count = 0
for i in range(n):
    a = int(input(f"Enter number {i + 1}: "))
    if a % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print(f"Even numbers: {even_count}, Odd numbers: {odd_count}")

