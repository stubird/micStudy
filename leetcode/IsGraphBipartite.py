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


def bipartite(graph):
    colors = [-1] * len(graph)
    cur_color = 1
    return all([dfs(graph, i, edges, colors, cur_color) for i, edges in enumerate(graph) if colors[i] == -1])

def dfs(graph, i, edges, colors, cur_color):
    if colors[i] == -1:
        colors[i] = cur_color
    else:
        if colors[i] != cur_color:
            return False
        else:
            return True

    return all([dfs(graph, j, graph[j], colors, not cur_color) for j in edges])

a = [[1,3], [0,2], [1,3], [0,2]]
a = [[1,2,3], [0,2], [0,1,3], [0,2]]
print(bipartite(a))
