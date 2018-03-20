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
str1 = "nvklksadidnv"
str2 = "jsalnvisdnsv"

array1 = [str1[i] for i in range(len(str1))]
array2 = [str2[i] for i in range(len(str2))]

maxlength = [[0 for _ in range(len(str1)+1)] for _ in range(len(str1)+1)]
record = [[0 for _ in range(len(str1)+1)] for _ in range(len(str1)+1)]

for i in range(len(str1)):
    for j in range(len(str2)):
        if str1[i] == str2[j]:
            maxlength[i+1][j+1] = maxlength[i][j] + 1
            record[i+1][j+1] = "arro"
        else:
            maxlength[i + 1][j + 1] = max(maxlength[i][j + 1], maxlength[i + 1][j])
            if maxlength[i][j + 1] > maxlength[i + 1][j]:
                record[i+1][j+1] = "  ^ "
            else:
                record[i + 1][j + 1] = " <- "

for i in maxlength:
    print(i)

i = len(array1)
j = len(array2)
strs=[]

while True:
    if i == 0 or j == 0:
        break
    if record[i][j] == "arro":
        i-=1
        j-=1
        strs.append(array1[i])
    elif record[i][j] == " <- ":
        j -= 1
    elif record[i][j] == "  ^ ":
        i -= 1

strs.reverse()
"".join(strs)
print("".join(strs))