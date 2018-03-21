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
given = [[1,3],[2,6],[8,10],[15,18]]


def merge(intervals):
    """
    :type intervals: List[Interval]
    :rtype: List[Interval]
    """
    if intervals == []:
        return []

    pre = [intervals[i][0] for i in range(len(intervals))]
    pre.sort()
    sec = [intervals[i][1] for i in range(len(intervals))]
    sec.sort()
    ret = []
    while True:
        a = pre.pop(0)
        b = sec.pop(0)
        if pre == []:
            ret.append([a, b if len(sec) == 0 else sec[-1]])
            break

        while b >= pre[0]:
            pre.pop(0)
            b = sec.pop(0)
            if len(pre) == 0:
                b = b if len(sec) == 0 else sec[-1]
                ret.append([a, b])
                return ret

        ret.append([a, b])
    return ret

print(merge(given))


