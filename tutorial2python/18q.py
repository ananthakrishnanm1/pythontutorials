def fact_rec(n):
    if n == 0 or n == 1:
        return 1
    return n * fact_rec(n - 1)

print(fact_rec(5))