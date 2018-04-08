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

def yieldsend():
    for i in range(3):
        print("start i=", i)
        y = yield i
        print("y=",y)
    yield 4

sender = yieldsend()

print("1s",sender.send(None))
print("***")
print("2s",sender.send(7))
print("***")
print("3s",sender.send(8))
sender.send(9)