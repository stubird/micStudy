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
import numpy as np
import gpoint as gp

class graph:
    def __init__(self, name = "graph"):
        self.name = name
        self.points = []
        self.root = []
        self.outonly = []

    def createRootByAry(self, array, outonly = {}, directed = False):
        if directed == True and len(outonly) == 0:
            raise TypeError("out only point of directed graph must explicit")
        if len(array) <= 0 or type(array[0]) != list:
            raise TypeError("Wrong shape of array")

        for i in outonly:
            self.outonly.append(gp.gpoint(i))

        for i in range(len(array)):
            if len(array[i]) > len(array):
                raise ValueError("links can't large than array dimension")
            if array[i] == [] and i not in outonly:
                self.outonly.append(gp.gpoint(i))

class bfsgraph(graph):
    def __init__(self, name = "bfsgraph"):
        #super(graph,self).__init__()
        graph.__init__(self,name)

    def createByAry(self, array, outonly = {}, directed = False):
        self.createRootByAry(array, outonly = {}, directed = False)
