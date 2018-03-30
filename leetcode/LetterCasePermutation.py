#784
strs = 'a2b4c4'

count = 0
for i in range(len(strs)):
    if strs[i].isalpha():
        count+=1

countnum = 2**count - 1

ret = []
while countnum >= 0:
    countnum_tmp = countnum
    zeros = [0 for i in range(count)]
    k = 0
    while countnum_tmp > 0:
        zeros[k] = countnum_tmp % 2
        countnum_tmp //= 2
        k+=1
    newstr = []
    j = -1
    for i in range(len(strs)):
        if strs[i].isalpha() and -j < len(zeros)+1 and zeros[j] == 1:
            newstr.append(strs[i].upper())
            j -= 1
        else:
            if strs[i].isalpha() and -j < len(zeros)+1:
                j -= 1
            newstr.append(strs[i])
    ret.append(newstr)
    countnum -= 1
print(ret)