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



