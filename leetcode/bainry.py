m=66
n=70

print(bin(n))
binn = bin(n)
if m - n >= len(binn) - 2:
    print(0)
else:
    for i in range(len(binn) - 1, len(binn) -1  - n + m , -1):
        j = 2**(len(binn) - 1 -i)
        if binn[i] == '1':
            n-=j
            print("sub",j)
print(n)