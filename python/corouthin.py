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
def consumer():
    n = ''
    i = 'k'
    while True:
        i = yield i
        if not i:
            return
        print('[CONSUMER] Consuming %s... %s' % (n,i))
        r = '200 OK'

def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send("".join(["huhu",str(n)]))
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()

c = consumer()
produce(c)
for i in consumer():
    print(i)
