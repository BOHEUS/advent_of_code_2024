a = []
b = []
sum = 0
with open('input.txt') as f:
    for line in f:
        a.append(int(line[:5]))
        b.append(int(line[-6:]))

a.sort()
b.sort()

for i in range(len(a)):
    sum+=b.count(a[i])*a[i]

print(sum)
