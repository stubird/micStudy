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
from 'Introduction to Algorithms'
"""
import random
from time import time

def countingsort(array):
    """
    :param array: integer array
    :return: sorted array
    """
    arraydict = {}
    maxnum = max(array)
    for i in range(maxnum):
        arraydict[i] = 0

    for i in array:
        arraydict[i-1] += 1

    sortlist = []
    for i in range(maxnum):
        for _ in range(arraydict[i]):
            sortlist.append(i+1)

    return  sortlist

length = 1000000
arraytoSort = [random.randint(1,10000) for _ in range(length)]

#print(countingsort(arraytoSort))
time1 = time()
countingsort(arraytoSort)
print(time() - time1)