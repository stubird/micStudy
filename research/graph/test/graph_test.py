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

import sys
sys.path.append("..")
#这里直接引用了文件
import graph as gh
import numpy as np

g = gh.graph()
grAry = [[1,2],[],[1,3,4],[4],[],[]]
g.createRootByAry(grAry)
for i in g.outonly:
    print(i.id)

gb = gh.bfsgraph()
print(gb.name)
gb.createByAry(grAry)
for i in gb.outonly:
    print(i.id)



