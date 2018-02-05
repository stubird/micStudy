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

"""
深度优先搜索，深度优先搜索树，图的邻接列表表示法
"""

class graph:
    def __init_(self, name = "graph"):
        self.name = name


class poi:
    def __init__(self, id, p = None,f = 0, d = 0, c = 'w'):
        self.id = id
        #parent
        self.p = p
        #start time
        self.d = d
        #end time
        self.f = f
        #color
        self.c = c
        self.link = []