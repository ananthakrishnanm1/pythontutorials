nums = [1, 3, 2, 4]
nums.sort()
n = len(nums)
if n % 2 == 1:
    median = nums[n // 2]
else:
    median = (nums[n // 2 - 1] + nums[n // 2]) / 2
print(median) 
