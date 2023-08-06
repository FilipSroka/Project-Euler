N = 600851475143

def is_prime(x):
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    return True
    
f = 1
for i in range(3, int(N**0.5)+1, 2):
    if N % i == 0:
        if is_prime(N/i):
            f = int(N/i)
            break
        elif is_prime(i):
            f = i

print(f)
        
