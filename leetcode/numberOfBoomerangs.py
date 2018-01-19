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
from leetcode:
Given n points in the plane that are all pairwise distinct, a "boomerang" 
is a tuple of points (i, j, k) such that the distance between i and j equals
the distance between i and k (the order of the tuple matters).

Find the number of boomerangs. You may assume that n will be at most 500 and
 coordinates of points are all in the range [-10000, 10000] (inclusive).
 
 see more detail:
 https://leetcode.com/problems/number-of-boomerangs/description/
"""

def findBoomerangs(points):
    setOfdistance = []
    for i in range(len(points)):
        for j in range(len(points)):
            if i != j:
                calpoint = points[j]
                distance = (points[i][0] - calpoint[0])**2 + (points[i][1] - calpoint[1])**2
                if len(setOfdistance) < i + 1:
                    setOfdistance.append([distance])
                else:
                    setOfdistance[i].extend([distance])
    return setOfdistance

points =[[1,0],[2,0],[222,0],[222,1],[24,0],[25,0]]
distanceSet = findBoomerangs([[1,0],[2,0],[222,0],[222,1],[24,0],[25,0]])
sumAll = 0
for x in distanceSet:
    x.sort()
    sum = 0
    step = 1
    for i in range(len(x)):
        if i + 1 == len(x) or x[i] != x[i+1]:
            if step > 1:
                step = step * (step - 1)
            else:
                step = 0
            sum = sum + step
            step = 1
        else:
            step = step + 1
    print(x, sum)
    sumAll = sumAll + sum

def numberOfBoomerangs(points):
    res = 0
    for p in points:
        cmap = {}
        for q in points:
            f = p[0]-q[0]
            s = p[1]-q[1]
            cmap[f*f + s*s] = 1 + cmap.get(f*f + s*s, 0)
        for k in cmap:
            res += cmap[k] * (cmap[k] -1)
        print(cmap)
    return res
print(sumAll)
print("hello")