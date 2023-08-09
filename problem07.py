def is_prime(n):
    for prime in primes:
        if prime * prime > n:
            break
        if n % prime == 0:
            return False
    return True
    
primes = [2]
n = 3
while len(primes) < 10001:
    if is_prime(n):
        primes.append(n)
    n += 2
print(primes[-1])
