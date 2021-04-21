a = str(input())  # уже не помню что это
v = [0]*len(a)
for i in range(1, len(a)):
    k = v[i-1]
    while k > 0 and a[k] != a[i]:
        k = v[k-1]
    if a[k] == a[i]:
        k = k + 1
    v[i] = k
print(v)