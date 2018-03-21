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
s="barfoothefoobarmanxfoobardnfooifoobar"
words = ["foo", "bar"]
qwords = words[:]
i = 0
indice = []
while True:
    if i >= len(s):
        break
    if s[i:i+3] in qwords:
        qwords.pop(qwords.index(s[i:i+3]))
        i+=3
        if qwords == []:
            indice.append(i - len(words[0])*len(words))
            qwords = words[:]
    elif len(qwords) < len(words):
        qwords = words[:]
        i += 1
    else:
        i+=1
print(indice)

class bintree:
    def __init__(self, val, name):
        self.left = None
        self.right = None
        self.val = val
        self.name = name
        self.layer = []

bintreearray = [5,3,7,2,4,6,8,1]
i = 0
def buildtree(array, index):
    root = bintree(array[index], name=index)
    if index*2+1 < len(bintreearray):
        root.left = buildtree(array, index*2+1)
    if index*2+2 < len(bintreearray):
        root.right = buildtree(array, index * 2 + 2)
    return root

def showtree(root, i=0, layer=[]):
    if len(layer)-1 <= i:
        layer.append([root.val])
    else:
        layer[i].append(root.val)
    if root.left != None:
        layer = showtree(root.left, i+1, layer)
    if root.right != None:
        layer = showtree(root.right, i+1, layer)
    return layer

def inordertreewalk(root):
    if root.left != None:
        inordertreewalk(root.left)
    print(root.val)
    if root.right != None:
        inordertreewalk(root.right)

def tree_search(root, x):
    if root == None or root.val == x:
        return root
    else:
        if x > root.val:
            return tree_search(root.right, x)
        else:
            return tree_search(root.left, x)


tree1 = buildtree(bintreearray,0)
print(showtree(tree1))
inordertreewalk(tree1)
print(tree_search(tree1, 3).name)


