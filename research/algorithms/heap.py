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
def left(i):
    return i*2

def right(i):
    return i*2+1

def heapify(a, i):
    lenght = len(a)
    largest = i
    if left(i) < lenght and a[left(i)] > a[i]:
        largest = left(i)
    if right(i) < lenght and a[right(i)] > a[largest]:
        largest = right(i)

    if largest != i:
        a[largest], a[i] = a[i], a[largest]
        heapify(a,largest)


a = ["",1,2,3,4,5,6,7,8,9]

#print(heapify(a,1))

for i in range(len(a)//2,0,-1):
    heapify(a,i)
    print(a)

print(a)

b=[]
while len(a) > 1:
    a[-1], a[1] = a[1], a[-1]
    b.append(a[-1])
    del a[-1]
    heapify(a,1)
print(b)
