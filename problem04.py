x = -1
for i in range(100, 1000):
    for j in range(i, 1000):
        n = str(i*j)
        if n == n[::-1]:
            x = max(x, i*j)
print(x)
            
