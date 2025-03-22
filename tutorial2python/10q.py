import re
pw = "Password123$"
is_valid = len(pw) >= 6 and \
          bool(re.search(r'[a-z]', pw)) and \
          bool(re.search(r'[A-Z]', pw)) and \
          bool(re.search(r'[0-9]', pw)) and \
          bool(re.search(r'[$#@]', pw))
print(is_valid)  
