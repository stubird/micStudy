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

a = [3,-2,-4,5,3,1,-4]

store = {}
store[-1] = float('-inf')
mdstore = float('-inf')

for i in range(len(a)):
    dot = 1
    maxdot = a[i]
    for j in range(i, -1, -1):
        dot *= a[j]
        maxdot = max(store[i-1], dot,maxdot)
        if maxdot != mdstore:
            process = (j,i)
            mdstore = maxdot

    store[i] = maxdot

#print(store,process)

strs = ['a','b','c','d']

keep = []
for i, c in enumerate(strs):
    out = 'ad'
    keep.append(c)
    if i == 0:
        out = c
        continue
    if i % 2 == 1:
        out = keep[0]
    else:
        del keep[0]
        out = keep[0]

    print(out)