s = "hello world"
v = 'aeiouAEIOU'
s = ''.join([c for c in s if c not in v])
print(s) 
