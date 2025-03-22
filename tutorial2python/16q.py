print("1. Check Even or Odd")
print("2. Check Positive, Negative or Zero")
print("3. Generate Factors of a Number")
ch = int(input("Enter choice: "))

if ch == 1:
    n = int(input("Enter a number: "))
    print("Even" if n % 2 == 0 else "Odd")
elif ch == 2:
    n = int(input("Enter a number: "))
    if n > 0:
        print("Positive")
    elif n < 0:
        print("Negative")
    else:
        print("Zero")
elif ch == 3:
    n = int(input("Enter a number: "))
    factors = [i for i in range(1, n + 1) if n % i == 0]
    print(f"Factors: {factors}")
else:
    print("Invalid choice")
