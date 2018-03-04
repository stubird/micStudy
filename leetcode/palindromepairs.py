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


def findpair(array, index):
    i = index + 1
    indexc = index
    remain = {i: '' for i in range(len(array))}
    del remain[index]
    j = -1
    while len(remain) != 0 and (-j <= len(array[index]) or (j == -1 and len(array[index]) == 0)):
        keys = [i for i in remain.keys()]
        # print(keys)
        # print(j)
        for i in keys:
            if (array[index] + array[i])[j] != (array[index] + array[i])[-(j + 1)]:
                del remain[i]
            elif len(array[index]) < len(array[i]):
                base = len(array[index])
                diff = len(array[i]) - len(array[index])
                for k in range(diff // 2):
                    word = array[index] + array[i]
                    if word[base + k] != word[-base - 1 - k]:
                        del remain[i]
                        break
        j -= 1
    return [[index, i] for i in remain.keys()]

words = ["a","abc","aba",""]
result = []
for i in range(len(words)):
    result += findpair(words, i)
print(result)