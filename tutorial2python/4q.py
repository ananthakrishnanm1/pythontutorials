s = "hello world"
if ' ' in s:
    s = s.replace(' ', '*')
else:
    s = f"${s}$"
print(s) 
