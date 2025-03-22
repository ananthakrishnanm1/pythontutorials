a = int(input("Enter lower limit: "))
b = int(input("Enter upper limit: "))
sum_odd = 0
for i in range(a, b + 1):
    if i % 2 != 0:
        sum_odd += i
print(f"Sum of odd numbers: {sum_odd}")

