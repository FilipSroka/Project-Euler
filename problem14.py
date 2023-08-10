n = -1
memo = {}

for i in range(1, 1000000):
    x = i
    count = 1
    while x != 1:
        if x in memo:
            count += memo[x]
            break
        if x % 2:
            x = 3 * x + 1
        else:
            x /= 2
        count += 1
    memo[i] = count
    if n < count:
        n, s = count, i

print(s)
