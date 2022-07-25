# list(map(int, input().split()))
a = [1, 3, 5, 6, 10]
b = []
if len(a) == 1:
    print(*a)
else:
    for i in a:
        if i == a[0]:
            b.append(a[1] + a[-1])
        elif i == a[-1]:
            b.append(a[-2] + a[0])
        else:
            b.append((a.index(i) - 1) + (a.index(i) + 1))

print(b)
