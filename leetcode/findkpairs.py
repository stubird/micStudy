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
Leetcode excise

You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.

Define a pair (u,v) which consists of one element from the first array and one element from the second array.

Find the k pairs (u1,v1),(u2,v2) ...(uk,vk) with the smallest sums.

https://leetcode.com/problems/find-k-pairs-with-smallest-sums/description/
"""
import math

def findkpair(array1, array2, k):
    # ar1map = {array1[i]:1 for i in range(k) if i < len(array1)}
    # ar2map = {array2[i]:2 for i in range(k) if i < len(array2)}
    # sortkeys1 = sorted(list(ar1map.keys()))
    if array1 == [] or array2 ==[]:
        return []

    index = [(0,0,array1[0] + array2[0])]
    dimension = 1
    ret = []
    k = min(k, len(array1) * len(array2))
    for i in range(k):
        cordinate = index[0]
        ret.append([array1[cordinate[0]], array2[cordinate[1]]])
        del index[0]
        if len(array1) > cordinate[0] + 1:
            unit = (cordinate[0] + 1, cordinate[1], array1[cordinate[0] + 1] + array2[cordinate[1]])
            if len(index) > 0:
                for x in range(len(index)):
                    if index[x][2] > unit[2]:
                        index = index[:x] + [unit] + index[x:]
                        unit = None
                        break
                if unit != None:
                    index.append(unit)
            else:
                index.append(unit)

        #update index
        if cordinate[0] == 0 and cordinate[1] + 1 < len(array2):
            unit = (0, cordinate[1] + 1, array1[0] + array2[cordinate[1] + 1])
            for x in range(len(index)):
                if index[x][2] > unit[2]:
                    index = index[:x] + [unit] + index[x:]
                    unit = None
                    break
            if unit != None:
                index.append(unit)
    return ret


a0 = findkpair([1,7,11,20,30], [2], 3)
print(a0,len(a0))