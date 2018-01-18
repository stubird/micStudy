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

from time import  time
from random import randint

def maxmumSub(array, curr, curp):
    if curr == curp:
        return array[curr], curp, curp
    if curp - curr == 1:
        if array[curp] * array[curr] > 0 and array[curr] > 0:
            return array[curp] + array[curr], curr, curp
        else:
            if array[curp] > array[curr]:
                return array[curp], curp, curp
            else:
                return array[curr], curr, curr

    mid = int((curr + curp)/2)

    max1, max1_r, max1_p, = maxmumSub(array, curr, mid)
    max2, max2_r, max2_p = maxmumSub(array, mid + 1, curp)

    maxAll, maxAll_r, maxAll_p = findMaxmunOfTwo(array, curr, mid, curp, max1, max1_r, max1_p, max2, max2_r, max2_p)
    #print(array,' r',curr,' mid', mid,' p', curp,' max1', max1,' max2', max2,' maxAll',maxAll,' maxAll_r', maxAll_r,' maxAll_p', maxAll_p)
    return maxAll, maxAll_r, maxAll_p

def findMaxmunOfTwo(array, r, mid, p, max1, max1_r, max1_p, max2, max2_r, max2_p):
    leftmax = float('-inf')
    tmpmax = 0
    leftindex = mid
    for i in range(mid , r - 1, -1):
        tmpmax = array[i] + tmpmax
        if tmpmax > leftmax:
            leftmax = tmpmax
            leftindex = i

    rightmax = float('-inf')
    tmpmax = 0
    rightindex = mid + 1
    for i in range(mid + 1, p+1, 1):
        tmpmax = array[i] + tmpmax
        if tmpmax > rightmax:
            rightmax = tmpmax
            rightindex = i

    centreMax = rightmax + leftmax
    maxval = max(centreMax, max1, max2)
    #print(centreMax, ' ', max1, ' ', max2)

    if maxval == max1:
        return maxval, max1_r, max1_p
    elif maxval == max2:
        return maxval, max2_r, max2_p
    elif maxval == rightmax + leftmax:
        return maxval, leftindex, rightindex

testTimes = 1
testArrayLen = 400
for i in range(testTimes):
    array = [randint(-50,50) for _ in range(testArrayLen)]
    value, index1, index2 = maxmumSub(array,0,len(array) - 1)
    #print(array, ' value',value, 'index1',index1, 'index2',index2)

    leng = len(array)
    r = 0
    p = 0
    maxmum = 0
    for i in range(leng):
        for j in range(leng):
            sum = 0
            for k in range(i, j+1):
                sum = sum + array[k]
            if sum > maxmum:
                maxmum = sum
                r = i
                p = j

    almax = 0
    for i in range(index1, index2 + 1,1):
        almax += array[i]

    if value != maxmum or almax != maxmum:
        print("search error: ")
    #print(maxmum, ' r:', r, ' p:',p)