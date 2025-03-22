def fact(n):
    if n == 0 or n == 1:
        return 1
    return n * fact(n - 1)

n = 5
r = 2
nCr = fact(n) // (fact(r) * fact(n - r))
print(nCr) 
