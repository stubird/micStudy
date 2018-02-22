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

def exchange(i, j, mat):
    mat[i][j], mat[j][-i-1], mat[-i-1][-j-1], mat[-j-1][i] = \
        mat[-j-1][i], mat[i][j], mat[j][-i-1], mat[-i-1][-j-1]

mat = [[1,2,3],
       [4,5,6],
       [7,8,9]]

mat.reverse()
print(mat)
mat = [
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
]
n = len(mat)
for i in range(n // 2):
    for j in range(i, n - i - 1):
        exchange(i, j, mat)

print(mat)
