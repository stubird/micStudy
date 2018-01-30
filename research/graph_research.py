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

import queue

class poi:
    def __init__(self, id, p = None, d = 0, c = 'w'):
        self.id = id
        self.p = p
        self.d = d
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

q = queue.Queue()

q.put_nowait(poiarray[1])


while not q.empty():
    poi = q.get_nowait()
    poi.c = 'b'
    for relpoi in poi.link:
        if relpoi.c == 'w':
            q.put_nowait(relpoi)
            relpoi.p = poi
            relpoi.d = poi.d + 1

for poi in poiarray:
    print(poi.c, poi.id, poi.p.id if poi.p != None else None, poi.d)