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
code for bucket sor
from 'Introduction of Algorithms'
"""
import  random

def bucketsort(array, bucketlen = 10):
    bucket = [[] for _ in range(bucketlen)]
    for i in array:
        bucket[int(i*10)].append(i)
    for i in bucket:
        insertsort(i)

    ret = []
    for w in bucket:
        ret.extend(w)
    return ret

def insertsort(array):
    for x in range(1, len(array)):
        for i in range(x - 1, -1, -1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
            else:
                break

array = [random.random() for i in range(20)]
ret = bucketsort(array)
print(ret)