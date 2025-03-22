def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

nums = [1, 2, 3, 4, 5]
primes = [n for n in nums if is_prime(n)]
composites = [n for n in nums if not is_prime(n)]
print(primes, composites) 
