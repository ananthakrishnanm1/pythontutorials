lst = [1, 2.5, "hello", 3]
ints = [x for x in lst if isinstance(x, int)]
flts = [x for x in lst if isinstance(x, float)]
strs = [x for x in lst if isinstance(x, str)]
print(ints, flts, strs) 
