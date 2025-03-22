s = "I like python programming"
words = ["python"]
s = ' '.join([w for w in s.split() if w not in words])
print(s) 
