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
#5
strs = "abbkadccdab"

#pd = [[False for i in range(len(strs))] for j in range(len(strs))]
pdindex = [[1 for _ in range(len(strs))] for _ in range(len(strs))]
#for i in range(len(strs)):
#    pd[i][i] = True

for i in range(len(strs)):
    for j in range(i, -1, -1):
        if i - j > 2:
            #pd[j][i] = True if pd[j+1][i-1] == True and strs[j] == strs[i] else False
            pdindex[j][i] = pdindex[j+1][i-1] + 2 if pdindex[j+1][i-1] == i-j-1 and strs[j] == strs[i]\
                else max(pdindex[j][i-1],pdindex[j+1][i])

        elif i - j == 1:
            #pd[j][i] = True if strs[j] == strs[i] else False
            pdindex[j][i] = pdindex[j+1][i] + 1 if strs[j] == strs[i] else pdindex[j+1][i]

for i in range(len(strs)):
    print(pdindex[i])

s = "babad"
pdindex = [[1 for _ in range(len(s))] for _ in range(len(s))]

for i in range(len(s)):
    for j in range(i, -1, -1):
        if i - j >= 2:
            pdindex[j][i] = pdindex[j + 1][i - 1] + 2 if pdindex[j + 1][i - 1] == i - j - 1 and s[j] == s[i] \
                else max(pdindex[j][i - 1], pdindex[j + 1][i])
        elif i - j == 1:
            pdindex[j][i] = pdindex[j + 1][i] + 1 if s[j] == s[i] else pdindex[j + 1][i]

s1 = 0
s2 = 0
h = len(s)
j = 0
i = h - 1
while True:
    if i < 1 or pdindex[j][i - 1] < pdindex[0][h-1]:
        while pdindex[j+1][i] == pdindex[0][h-1]:
            j+=1
        else:
            break
    i -= 1

print(s[j:i+1])

for i in range(len(s)):
    print(pdindex[i])