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
top - down
"""

prize = [0, 1 ,5, 8, 9, 10, 17, 17, 20, 24, 30]
lenght = 30

values = {}
for i in range(lenght+1):
    values[i] = -1

def cutrod(p, l):
    """
    :param p: prize array
    :param n: max value when cut on n
    :param l: lenght of rod
    :return: value
    """

    if values[l] >= 0:
        return values[l]

    value = 0
    if l <= 10:
        value = prize[l]
    for i in range(1,l,1):
        value = max(value, cutrod(p, i) + cutrod(p, l - i))
        print(i, l ,value)
    values[l] = value
    return value

print(cutrod(prize, lenght), values)