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
Simple Insert sort
"""
from random import random
from time import time

length = 10000
arraytoSort = [ int(random()*100) for _ in range(length)]

result = [arraytoSort.pop()]

timepoint = time()
for x in arraytoSort:
    for y in range(len(result)):
        if x <= result[y]:
            newr = result[0:y]
            newr.extend([x])
            newr.extend(result[y:])
            result = newr
            break
        if  y == len(result) - 1:
            result.extend([x])

timepoint =  time() - timepoint

# print("orgin",arraytoSort)
# print("sorted",result)
print(timepoint)