sum_pos = 0
sum_neg = 0
count_pos = 0
count_neg = 0
for i in range(4):
    a = int(input(f"Enter number {i + 1}: "))
    if a > 0:
        sum_pos += a
        count_pos += 1
    elif a < 0:
        sum_neg += a
        count_neg += 1
if count_pos > 0:
    avg_pos = sum_pos / count_pos
else:
    avg_pos = 0
if count_neg > 0:
    avg_neg = sum_neg / count_neg
else:
    avg_neg = 0
print(f"Sum of positive numbers: {sum_pos}, Average of positive numbers: {avg_pos}")
print(f"Sum of negative numbers: {sum_neg}, Average of negative numbers: {avg_neg}")

