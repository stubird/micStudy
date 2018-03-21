
a = [4,3,1,1,0,0,3]
store = []
for i in range(len(a)-1,-1,-1):
    if a[i] > len(store):
        store = []
        continue
    else:
        store.append(1)
print(len(store))