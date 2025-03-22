a = int(input("Enter a number: "))
b = len(str(a))
c = a
d = 0
while c > 0:
    e = c % 10
    d += e ** b
    c //= 10
if d == a:
    print(f"{a} is an Armstrong number")
else:
    print(f"{a} is not an Armstrong number")

