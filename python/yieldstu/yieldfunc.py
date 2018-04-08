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
import time
import asyncio

def another():
    for i in range(2):
        yield i
    return "xixi"

@asyncio.coroutine
def producer():
    print("product")
    for i in range(4):
        print("before yield")
        line = yield from another()
        print("after yield ",line)

@asyncio.coroutine
def producerf():
    print("fff!!!")
    susu = yield from producerk()
    print(susu)

@asyncio.coroutine
def producerk():
    print("KKK!!!")
    return "sisi"

loop = asyncio.get_event_loop()
tasks = [producerf() for _ in range(3)]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()


