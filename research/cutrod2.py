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
from Introduction to Algorithms
dynamic programming ---- cut rod memorized
down to top
"""
prize = [0, 1 ,5, 8, 9, 10, 17, 17, 20, 24, 30]
lenght = 30

r = {i:0 for i in range(lenght+1)}
r[0] = 0
r[1] = prize[1]
for i in range(1,lenght+1,1):
    maxvalue = prize[i] if i <= 10 else 0
    for j in range(1,i,1):
        maxvalue = max(maxvalue, r[j] + r[i - j])
    r[i] = maxvalue
print(r)