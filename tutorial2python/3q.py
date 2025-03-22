s = "madam"
l = len(s)
is_palindrome = True
for i in range(l // 2):
    if s[i] != s[l - i - 1]:
        is_palindrome = False
        break
print(is_palindrome)  
