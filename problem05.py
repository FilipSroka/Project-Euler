def checker(n):
    for i in range(1, 21):
        if n % i != 0:
            return False
    return True

n = 20
while True:
    if checker(n):
        print(n)
        break
    n += 20
        
