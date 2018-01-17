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

from random import random
from time import time

#sort use prediction methods
#base on insertion sort

def perdict(list, value):
    endpoint = len(list) - 1
    middlepoint = int(endpoint / 2)
    bias = list[0]
    numgap1 = (list[endpoint] - list[middlepoint])
    numgap1 = numgap1 + 1 if numgap1 >= 0 else numgap1 - 1
    numgap2 = (list[middlepoint] - list[0])
    numgap2 = numgap2 + 1 if numgap2 >= 0 else numgap2 - 1

    k1 = (endpoint - middlepoint + 1) / numgap1
    k2 = (middlepoint) / numgap2

    ret = int((value - bias) * (k1 / 2 + k2 / 2))
    if ret < 0:
        return 0
    elif ret > endpoint:
        return endpoint
    return ret

length = 10000
arraytoSort = [int(random()*1000) for _ in range(length)]
orgin = arraytoSort[:]

timepoint = time()
count = 0
for x in range(1, len(arraytoSort)):
    right = x
    left = x
    sign = arraytoSort[x]

    predictPoint = perdict(arraytoSort[:x], arraytoSort[x])

    if arraytoSort[predictPoint] <= sign:
        while True:
            count = count + 1
            left = predictPoint
            if arraytoSort[predictPoint] > sign or predictPoint == 0:
                predictPoint = predictPoint + 1
                break
            predictPoint = predictPoint - 1

    else:
        while True:
            count = count + 1
            left = predictPoint
            if arraytoSort[predictPoint] < sign or predictPoint == x:
                break
            predictPoint = predictPoint + 1

    first = arraytoSort[:left]
    middle = arraytoSort[left:right]
    end = arraytoSort[right+1:]

#    print("orgin", arraytoSort)
#    print(first, ' ', middle, ' ',end, 'sign',sign,'\n')

    first.extend([sign])
    first.extend(middle)
    first.extend(end)
    arraytoSort = first

timepoint =  time() - timepoint

#print("orgin",orgin)
#print("sorted",arraytoSort)
sorts = arraytoSort
sorts.sort(reverse=True)
for x in range(len(arraytoSort)):
    if sorts[x] != arraytoSort[x]:
        print("false")

print('time spend ',timepoint,' loop times', count)

print(perdict([x for x in range(0,-100,-1)],10))