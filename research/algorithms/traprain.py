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

a = [0,1,0,2,1,0,1,3,2,1,2,1]
pre = a[0]
water = []
sums = 0
l=0
r=len(a) - 1
lmax = 0
rmax = 0
while l < r:
    lmax = max(a[l], lmax)
    rmax = max(a[r], rmax)
    if lmax < rmax:
        sums += lmax - a[l]
        l+=1
    else:
        sums += rmax - a[r]
        r -= 1


print(sums)


