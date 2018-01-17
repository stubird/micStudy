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

import random
from time import time
import sys
import numpy as np

length = 300000
arraytoSort = [int(random.random()*1000) for _ in range(length)]
orgin = arraytoSort[:]
sys.setrecursionlimit(length)

def partition(array, p, r):
    i = p
    j = p

    # a optimal method, original quick sort exclude this method
    if r - p > length/100:
        rand1 = random.randint(p, r)
        rand2 = random.randint(p, r)
        rand3 = random.randint(p, r)
        indexrand = [rand1, rand2, rand3]
        sortindex = [array[rand1], array[rand2], array[rand3]]
        index = np.argsort(sortindex,axis=0)
        point = indexrand[index[1]]
        #print(rand1,' ', rand2,' ', rand3,' p',point,' ')
        #print(array[rand1], array[rand2], array[rand3])
        array[point], array[r] = array[r], array[point]
    # optimal method end

    compare = array[r]
    while j < r:
        if array[j] < compare:
            array[i], array[j] = array[j], array[i]
            i = i + 1
        j = j + 1
    array[i] , array[r] = array[r], array[i]
    return i


def quicksort(array, p, r):
    if p >= r:
        return
    q = partition(array,p,r)
    quicksort(array,p,q - 1)
    quicksort(array,q+1,r)

#test time spend
#print(arraytoSort)
timepoint = time()
quicksort(arraytoSort,0,len(arraytoSort) - 1)
print(time() - timepoint)
#print(arraytoSort)