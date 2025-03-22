a = int(input("Enter time in seconds: "))
b = a // 3600
c = (a % 3600) // 60
d = a % 60
print(f"{b:02}:{c:02}:{d:02}")

