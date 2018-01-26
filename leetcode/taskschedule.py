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
leetcode study:

Task Scheduler

https://leetcode.com/problems/task-scheduler/description/
"""

array = ["A","A","A","A","B","B","B","B","B","C","C","C","C"]

# statics numbers of each captain letter
dictarray = {}
for i in array:
    dictarray[i] = dictarray[i] + 1 if i in dictarray else 1

maxunit = max(dictarray.values())

cout = 0
for i in dictarray:
    if maxunit == dictarray[i]:
        cout += 1
k = 2
ret = max(len(array), (maxunit - 1)*(k + 1) + cout)
print(dictarray, maxunit, ret)