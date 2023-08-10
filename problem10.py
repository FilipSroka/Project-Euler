def is_prime(primes, n):
    for prime in primes:
        if prime * prime > n:
            return True
        if n % prime == 0:
            return False
       
N = 2000000
primes = [2]
prime = 3

while prime < N:
    if is_prime(primes, prime):
        primes.append(prime)
    prime += 2
    
print(sum(primes))
