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

a = '40.125'

aay = a.split('.')
intp = int(aay[0])
potp = float('.'+ aay[1])

retint = []
while intp >= 1:
    i = intp%2
    retint.append(str(i))
    intp = (intp - i)//2

retint.reverse()

retpot = []
i = 1
while i <= 32 and potp != 0:
    if (1/2)**i > potp:
        retpot.append(str(0))
    else:
        retpot.append(str(1))
        potp -= (1/2)**i
    i+=1

print(retpot)

x = 345345
while x > 2:
    print(x)
    x //= 2

print(x)
