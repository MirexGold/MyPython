a = [3, 2, 1, 4, 6, 8]
b = []
if len(a) == 1:
    print(*a)
else:
    for i in a:
        if i == a[0]:
            b.append(a[i+1]+a[-1])
print(b)


 # ([i + 1])+ ([-1])

