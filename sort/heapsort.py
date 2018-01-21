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

heap sort
    
    we build a binary tree to help sort
"""
import random
import time

def heapile(array, root):
    left = 2*root + 1
    right = 2*root + 2
    # print(array)
    # print("left",left,"val:",array[left] if left < len(array) else None,", right",right,"val:",array[right] if right < len(array) else None,
    #       left < len(array), right < len(array),"root:",root,"val:",array[root])
    maxnum = max(array[root],\
                 array[left] if left < len(array) else float('-inf'),\
                 array[right] if right < len(array) else float('-inf'))

    if maxnum == array[root]:
        return
    if left < len(array) and maxnum == array[left]:
        array[left], array[root] = array[root], array[left]
        heapile(array, left)
    elif right < len(array) and maxnum == array[right]:
        array[right], array[root] = array[root], array[right]
        heapile(array, right)

def heapilesorttime(array, root, k):
    left = 2*root + 1
    right = 2*root + 2
    # print(array)
    # print("left",left,"val:",array[left] if left < len(array) else None,", right",right,"val:",array[right] if right < len(array) else None,
    #       left < len(array), right < len(array),"root:",root,"val:",array[root])
    maxnum = max(array[root],\
                 array[left] if left < k else float('-inf'),\
                 array[right] if right < k else float('-inf'))

    if maxnum == array[root]:
        return
    if left < k and maxnum == array[left]:
        array[left], array[root] = array[root], array[left]
        heapilesorttime(array, left, k)
    elif right < k and maxnum == array[right]:
        array[right], array[root] = array[root], array[right]
        heapilesorttime(array, right, k)

def buildheap(array):
    lenght = len(array)
    lastbranchpoint = int(lenght / 2) - 1
    for x in range(lastbranchpoint, -1, -1):
        heapile(array,x)

def heapsort(array):
    for i in range(len(array)):
        array[0], array[len(array)-1-i] = array[len(array)-1-i], array[0]
        heapilesorttime(array,0, len(array) - i - 1)

def testifheapisright(array,root = 0):
    """
    :param array: the array to test
    :param root: test node
    :return: void
    test if the heap array is correctly build
    """
    left = 2*root + 1
    right = 2*root + 2
    if left < len(array) and array[root] > array[left]:
        testifheapisright(array, left)
    elif left < len(array) and array[root] < array[left]:
        print("left bigger than root")

    if right < len(array) and array[root] > array[right]:
        testifheapisright(array, right)
    elif right < len(array) and array[root] < array[right]:
        print("left bigger than root")

def testorder(array):
    for x in range(len(array)-1):
        if array[x] > array[x+1]:
            print("sort error")

test = [random.randint(0,100) for _ in range(300000)]

time1 = time.time()
buildheap(test)
#testifheapisright(test)
heapsort(test)
print(time.time() - time1)
testorder(test)