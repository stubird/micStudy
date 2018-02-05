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
deep first search graph
"""
import queue

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

# define a graph
graph_matrix = [[0,1,0,0,0,0],
                [1,0,1,0,1,0],
                [0,1,0,1,0,0],
                [0,0,1,0,1,0],
                [0,1,0,1,0,1],
                [0,0,0,0,1,0]]

poiarray = []
for i in range(len(graph_matrix)):
    poiarray.append(poi(i))
    for j in range(len(graph_matrix[i])):
        if graph_matrix[i][j] == 1:
            poiarray[i].link.append(j)

for x in poiarray:
    pois = []
    for index in x.link:
        pois.append(poiarray[index])
    x.link = pois[:]

time = 0

def visit(poi):
    global time
    poi.c = 'g'
    time += 1
    poi.d = time
    for son in poi.link:
        if son.c == 'w':
            son.p = poi
            visit(son)
    poi.c = 'b'
    time += 1
    poi.f = time

visit(poiarray[1])

for i in poiarray:
    print("p:{} link:{} d:{} f:{} id:{} c:{}".format(i.p.id if i.p != None else None,[poi.id for poi in i.link],i.d,i.f,i.id,i.c))


