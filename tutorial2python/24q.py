from collections import Counter
nums = [1, 2, 2, 3, 3, 3]
count = Counter(nums)
max_count = max(count.values())
mode = [n for n, f in count.items() if f == max_count]
print(mode) 
