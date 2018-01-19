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
leetcode:

Given a binary array, find the maximum length of a contiguous subarray 
with equal number of 0 and 1.

https://leetcode.com/problems/contiguous-array/description/
"""

def findMaxLength(nums):
    sum = 0
    recordpn = {}
    recordnn = {}
    maxval = 0
    for x in range(len(nums)):
        if nums[x] == 1:
            sum += 1
            recordpn[sum] = recordpn.get(sum,x)
        else:
            sum -= 1
            recordnn[sum] = recordnn.get(sum,x)

        if nums[x] == 1:
            print(maxval, x - recordnn.get(sum - 1, float('inf')), x - recordpn.get(sum + 1, float('inf')))
            maxval = max(maxval, x - recordnn.get(sum - 1,float('inf')), x - recordpn.get(sum + 1,float('inf')))
        else:
            print(maxval, x - recordpn.get(sum + 1, float('inf')), x - recordnn.get(sum - 1, float('inf')))
            maxval = max(maxval, x - recordpn.get(sum + 1, float('inf')), x - recordnn.get(sum - 1, float('inf')))
        print('sum',sum)

    return maxval + 1 if maxval > 0 else 0

print(findMaxLength([1,1,0,0,1,0]))