class node:
    def __init__(self, val):
        self.next = None
        self.val = val

class Getoutofloop(Exception):
    pass

try:
    k =3
    one = node(None)
    store = one
    for i in range(8):
        one.next = node(i+1)
        one = one.next

    havedo = False
    while True:
        one = l = r = store
        store1 = store
        for i in range(k):
            if l.next == None:
                raise Getoutofloop
            l = l.next

        cur = cur_store = r.next
        pre = r
        print("1  cur:{},pre:{},cur.next:{}".format(cur.val, pre.val, cur.next.val))
        for i in range(k-1):
            print("2  cur:{},pre:{},cur.next:{}".format(cur.val, pre.val, cur.next.val))
            cur.next,pre,cur = pre,cur,cur.next
            print("2  change: cur:{},pre:{},cur.next:{}".format(cur.val,pre.val,cur.next.val))

        cur_store.next, r.next , cur.next = cur.next, cur , pre
        if havedo == False:
            havedo = True
            store1.next = cur_store
        print("1  cur:{},pre:{},cur.next:{}".format(cur.val, pre.val, cur.next.val))
        pre = cur
        while pre != None:
            print(pre.val)
            pre = pre.next
        print("a loop")
except Getoutofloop:
    print("loop end")

    while store1 != None:
        print(store1.val)
        store1 = store1.next
# for i in range(8):
#     store = store.next
#     print(store.val)
