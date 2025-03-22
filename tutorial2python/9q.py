s = "abcdef"
m = len(s) // 2
s = s[:m][::-1] + s[m:][::-1]
print(s)  
