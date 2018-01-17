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

def divideRes(A,a,b,target):
    if A[a] == target:
        return a
    if A[b] == target:
        return b
    if a >= b:
        return "have no member"

    index = int((a+b)/2)
    if A[index] > target:
        b = index
    else:
        a = index

    return divideRes(A, a, b, target)

length = 1000000
testarray = [random.randint(0,100) for x in range(length)]
testarray.sort()
for i in range(length):
    n = divideRes(testarray, 0, length - 1, testarray[i])
    if i != n\
            and testarray[i] != testarray[n]:
        print(False, divideRes(testarray, 0, length - 1, testarray[i]), ' i',i)