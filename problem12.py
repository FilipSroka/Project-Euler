N = 500
i = 1
count = 0
n = -1

while count <= N:
    count = 0
    n = i * (i + 1) // 2
    for j in range(1, int(n**0.5)+1):
        if n % j == 0:
            count += 2
    i += 1
    
print(n)
