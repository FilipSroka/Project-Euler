total = 0

for i in range(0, 1000, 3):
    total += i
    
for i in range(0, 1000, 5):
    total += i

for i in range(0, 1000, 15):
    total -= i

print(total)
