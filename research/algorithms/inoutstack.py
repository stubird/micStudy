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
one = "ABCDEFG"
#two = "BAEDFGC"
two = "CEFDGAB"

# stack = []
# j = 0
# i = 0
# while j < len(two):
#     if i < len(one)  and (stack == [] or stack[-1] != two[j]):
#         stack.append(one[i])
#         i+=1
#     else:
#         if two[j] != stack.pop():
#             print("can't")
#             break
#         j += 1

array1 = [one[i] for i in range(len(one))]
array2 = [two[i] for i in range(len(two))]

tmp = []
while array1 != []:
    if tmp != [] and tmp[-1] == array2[0]:
        array2.pop(0)
        tmp.pop()
        continue
    tmp.append(array1.pop(0))

while tmp != []:
    if tmp[-1] == array2[0]:
        array2.pop(0)
        tmp.pop()
    else:
        print("can't stack")
        break

print(array2, tmp)
