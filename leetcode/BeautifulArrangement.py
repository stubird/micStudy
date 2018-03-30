n = 6
k = 4
a = [i for i in range(1,n+1)]
w = 1

k -= 1
print(k)
while k > 0:
    if k > 1:
        a = a[:w] + [a[-1]] + a[w:n-1]
        w+=2
        k-=2
    else:
        a = a[:-2] + [a[-1]] + a[-2:-1]
        k-=1

print(a)
