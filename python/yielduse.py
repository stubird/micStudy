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

def yields():
    n = 'gg'
    for i in range(100):
        k = yield n
        print('jm',k)

j=0
for i in yields():
    print('printi',j)
    j+=1

c = yields()
c.send(None)
for j in range(3):
    ret = c.send(44)
    print('ret',ret)
c.close()