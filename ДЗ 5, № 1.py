n = int(input())
sities = []
count = 0
for i in range(n):
    sity = input()
    if sity in sities:
        count += 1
    else:
        sities.append(sity)
print(count)
