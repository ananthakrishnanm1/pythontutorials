a = int(input("Enter base (X): "))
b = int(input("Enter exponent (Y): "))
c = 1
for i in range(b):
    c *= a
print(f"{a}^{b} = {c}")

