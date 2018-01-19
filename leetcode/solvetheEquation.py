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
leetcode:
Solve a given equation and return the value of x in the form of string "x=#value". 

The equation contains only '+', '-' operation, the variable x and its coefficient.

If there is no solution for the equation, return "No solution".

If there are infinite solutions for the equation, return "Infinite solutions".

If there is exactly one solution for the equation, we ensure that the value of x is an integer.

from

https://leetcode.com/problems/solve-the-equation/description/
"""
def calequation(strs):
    ret = strs.split('=')
    print(ret)
    print(ret[0], ret[1])
    an, anx = parseequ(ret[0])
    bn, bnx = parseequ(ret[1])

    if an == bn and anx == bnx:
        return 'Infinite solutions'
    elif anx == bnx and an != bn:
        return 'No solution'
    else:
        print(an , anx,bn  , bnx)
        return (an - bn) / (bnx - anx)
def parseequ(strs):
    num = 0
    xnum = 0
    sign = 1
    i = 0
    while i < len(strs):
        print("ddd",i)
        if strs[i] == 'x':
            xnum+=1*sign
        elif strs[i] == '-':
            sign = -1
        elif strs[i] == '+':
            sign = 1
        else:
            j = 0
            tmpnum = 0
            while i + j < len(strs) and strs[i+j] <= '9' and strs[i+j] >= '0':
                tmpnum = tmpnum*(10) + int(strs[i+j])
                j += 1
            if len(strs) > i+j and strs[i+j] == 'x':
                xnum+=sign*tmpnum
                i += 1
            else:
                num += tmpnum*sign
            i = i + j - 1 if j != 0 else i
        i += 1
    return num,xnum

print(calequation("x+5-3+x=6+x-2"))