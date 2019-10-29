result = []
total = 0

for i in range(0, 1000):
    if i % 3 == 0:
        result.append(i)
    elif i % 5 == 0:
        result.append(i)
for k in result:
    total += k

print(total)