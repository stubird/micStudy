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

"""leetcode problem:

Given a binary tree, imagine yourself standing on the right side of it,
return the values of the nodes you can see ordered from top to bottom.

https://leetcode.com/problems/binary-tree-right-side-view/description
"""


class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        if target >= letters[-1]:
            return letters[0]
        elif target < letters[0]:
            return letters[0]
        else:
            return self.divfind(target, letters)

    def divfind(self, target, letters):
        print(target, letters)
        if len(letters) == 1 and letters[0] >= target:
            return letters[0]
        if len(letters) == 2 and letters[0] > target and letters[0] <= letters[1]:
            return letters[0]
        elif len(letters) == 2:
            return letters[1]

        length = len(letters)
        if letters[int(length / 2)] > target:
            return self.divfind(target, letters[:int(length / 2) + 1])
        else:
            return self.divfind(target, letters[int(length / 2) + 1:])






sol = Solution()
letter = sol.nextGreatestLetter(["c","f","j"],
"c")



print(letter)