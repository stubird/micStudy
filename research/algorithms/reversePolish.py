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
strs='a+b*(c+d)/5-3'

numq = []
opq = []
propri = {'/':1,'*':1,'+':2,'-':2,'(':3,')':3}
for i in range(len(strs)):
    c = strs[i]
    if c.isalnum():
        numq.append(c)
    elif opq == [] or c == '(':
        opq.append(c)
    elif c == ')':
        d = opq[-1]
        while d != '(':
            numq.append(opq.pop())
            d = opq[-1]
        else:
            opq.pop()
    elif propri[c] > propri[opq[-1]]:
        while propri[c] > propri[opq[-1]]:
            numq.append(opq.pop())
        opq.append(c)
    elif propri[c] <= propri[opq[-1]]:
        opq.append(c)

while opq != []:
    numq.append(opq.pop())

print(numq)
