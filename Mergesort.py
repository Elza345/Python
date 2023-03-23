a = [-8, 0, 9, 12, 15, 55]
b = [2, 8, 14, 22 ]
c = []

N = len(a)
M = len(b)

i = 0
j = 0

while i < N and j < M:
    if a[i] <= b[j]:
        c.append(a[i])
        i += 1
    else:
        c.append(b[j])
        j += 1

c += a[i:] + b[j:]
print(c)
