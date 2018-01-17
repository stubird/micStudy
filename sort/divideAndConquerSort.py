"""
   Copyright 2018 (c) Jinxin Xie

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""

#divide-and-conquer sort
import random
from time import time
import sys

length = 100000
arraytoSort = [int(random.random()*1000) for _ in range(length)]
orgin = arraytoSort[:]
sys.setrecursionlimit(length)
count = 0

def divConSort(A):
    if len(A) == 2:
        if A[0] > A[1]:
            A[0], A[1] = A[1], A[0]
        return A
    elif len(A) == 1:
        return A

    mid = int(len(A) / 2)
    a1 = A[:mid]
    a2 = A[mid:]


    a1Sorted = divConSort(a1)
    a2Sorted = divConSort(a2)
    #print('a1Sorted',a1Sorted)
    #print('a2Sorted',a2Sorted)

    return merge(a1Sorted, a2Sorted)

def merge(a1, a2):
    i = -len(a2)
    while i < 0:
        if len(a1) == 0:
            break
        if a1[0] <= a2[i]:
            global count
            a2_tmp = a2[:i]
            j = 0
            while len(a1) > j and a1[j] <= a2[i]:
                count = count + 1
                j = j + 1
            a2_tmp.extend(a1[:j])
            a1 = a1[j:]
            a2_tmp.extend(a2[i:])
            a2 = a2_tmp
        else:
            i = i + 1

    a2.extend(a1)
    return a2

timepoint = time()
newsort = divConSort(arraytoSort)
print(time() - timepoint)

#print("orgin",orgin)
arraytoSort.sort()
#print("sorted",arraytoSort)
#print("sorted",newsort)

for x in range(len(arraytoSort)):
    if newsort[x] != arraytoSort[x]:
        print("false", newsort[x],' ',arraytoSort[x])
        pass

print('loop times', count)


