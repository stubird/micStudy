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
A self-dividing number is a number that is divisible by every digit it contains.

For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.

https://leetcode.com/problems/self-dividing-numbers/description/
"""


def selfDividingNumbers(left, right):
    """
    :type left: int
    :type right: int
    :rtype: List[int]
    """
    list = []
    for i in range(left, right + 1):

        num = i
        while True:
            if num % 10 == 0 or i % (num % 10) != 0:
                break
            else:
                num = int(num / 10)
                if num == 0:
                    list.append(i)
                    break

        return list