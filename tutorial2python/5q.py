s = "abcdef"
odd = ''.join([s[i] for i in range(1, len(s), 2)])
even = ''.join([s[i] for i in range(0, len(s), 2)])
print(odd, even)  
