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
#787
import collections
import heapq

def findCheapestPrice(self, n, flights, src, dst, k):
    f = collections.defaultdict(dict)
    for a, b, p in flights:
        f[a][b] = p
    heap = [(0, src, k + 1)]
    while heap:
        p, i, k = heapq.heappop(heap)
        if i == dst:
            return p
        if k > 0:
            for j in f[i]:
                heapq.heappush(heap, (p + f[i][j], j, k - 1))
    return -1