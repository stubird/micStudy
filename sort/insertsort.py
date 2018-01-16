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

"""
Simple Insert sort
"""
from random import random
from time import time

length = 10000
arraytoSort = [ int(random()*1000) for _ in range(length)]
orgin = arraytoSort[:]

#because big array item swap operation, the algorithm is not efficient in python
timepoint = time()
count = 0
for x in range(1, len(arraytoSort)):
    for i in range(x-1,-1,-1):
        count = count + 1
        if arraytoSort[i] > arraytoSort[i+1]:
            arraytoSort[i],arraytoSort[i+1] = arraytoSort[i+1],arraytoSort[i]
        else:
            break

timepoint =  time() - timepoint

#print("orgin",arraytoSort)
#print("sorted",orgin)
print('time spend ',timepoint,' loop times', count)

#use orgin array
arraytoSort = orgin[:]
result = [arraytoSort.pop()]

# better efficient but use a middle array which means more space used
timepoint = time()
count = 0
for x in arraytoSort:
    for y in range(len(result)):
        count = count + 1
        if x <= result[y]:
            newr = result[0:y]
            newr.extend([x])
            newr.extend(result[y:])
            result = newr
            break
        if  y == len(result) - 1:
            result.extend([x])

timepoint =  time() - timepoint

# print("orgin",arraytoSort)
# print("sorted",result)
print('time spend ',timepoint,' loop times', count)

#use orgin array
arraytoSort = orgin[:]

# more efficient
timepoint = time()
count = 0
for x in range(1, len(arraytoSort)):
    right = x
    left = x
    sign = arraytoSort[x]
    for i in range(x-1,-1,-1):
        count = count + 1
        if arraytoSort[i] < sign:
            left = i
        else:
            break

    first = arraytoSort[:left]
    middle = arraytoSort[left:right]
    end = arraytoSort[right+1:]

    first.extend([sign])
    first.extend(middle)
    first.extend(end)
    arraytoSort = first

timepoint =  time() - timepoint

#print("orgin",orgin)
#print("sorted",arraytoSort)
print('time spend ',timepoint,' loop times', count)