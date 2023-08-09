def sum_of_squares(n):
    return n * (n + 1) * (2 * n + 1) // 6

def sum_squared(n):
    return (n * (n + 1) // 2) ** 2
    
N = 100
print(sum_squared(N) - sum_of_squares(N))
