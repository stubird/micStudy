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
class trie():
    def __init__(self, val, isword = False, child = None):
        self.isword = isword
        self.val = val
        self.children = {}
        if child != None:
            self.children[child.val] = child

    @staticmethod
    def buildtrie(word, root = None):
        if root == None:
            root = trie('root')
        lastchild = root
        for i in range(31,-1,-1):
            lastunit = (word >> i) % 2
            if lastunit not in lastchild.children:
                lastchild.children[lastunit] = trie(lastunit)
            lastchild = lastchild.children[lastunit]
        lastchild.isword=True
        return root

    @staticmethod
    def buildarray(array, root = None):
        for i in array:
            root = trie.buildtrie(i, root)
        return root

    def __str__(self, pad = ""):
        strs =  "\n" + pad + "val = {0}, isword:{1}".format(self.val, self.isword) + "\n"
        strs += pad + "children dict: {0}".format(self.children.keys()) + "\n"
        for i in self.children:
            strs += pad + "children {0}:{1}".format(i, self.children[i].__str__(pad + "    ")) + "\n"

        return strs

nums = [3,4,10]
node = trie.buildarray([3,4,10,25,5])
#print(node)
result = 0

for num in nums:
    root = node
    maxnum = 0
    for i in range(31, -1, -1):
        sign = (num >> i) % 2
        if root.children != {} and sign^1 in root.children:
            maxnum += 1 << i
            root = root.children[sign^1]
        elif root.children != {}:
            root = root.children[sign]
    result = max(maxnum, result)

print(result)

