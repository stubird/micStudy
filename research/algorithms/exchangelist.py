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
class listnode(object):
    def __init__(self,val):
        self.val = val
        self.next = None

troot = listnode(1)
root = troot
for i in range(2,9):
    root.next = listnode(i)
    root=root.next

root = troot
for i in range(0,8):
    print(root.val)
    root=root.next

root = troot

def exchangeit(node):
    if node == None:
        return None
    nodesnext = node.next
    node.next = exchangeit(nodesnext.next)
    nodesnext.next = node

    return nodesnext
prenode = exchangeit(root)
while prenode != None:
    print(prenode.val)
    prenode = prenode.next