import heapq

def printl(node):
    c=node
    while c:
        print('%s->'%c.val, end='') 
        c=c.next
    print('NULL')

class Node:
    def __init__(self, val):
        self.val=val
        self.prev=None
        self.next=None

class LRUCache:
        
        
    # @param capacity, an integer
    def __init__(self, capacity):
        self._m={}
        self._lm={}
        self._cap=capacity
        self._head=None
        self._tail=None

    # @return an integer
    def get(self, key):
        try:
            val=self._m[key]
            node=self._lm[key]
            if node!=self._tail:
                if node==self._head:
                    self._head=self._head.next
                if node.prev:
                    node.prev.next=node.next
                if node.next:
                    node.next.prev=node.prev
                self._tail.next=node
                node.prev=self._tail
                self._tail=node
                node.next=None
            return val
        except KeyError:
            return -1

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if not self._m:
            node=Node(key)
            self._lm[key]=node
            self._head=self._tail=node
        else:
            if key in self._m:
                node=self._lm[key]
                if node!=self._tail:
                    if node==self._head:
                        self._head=self._head.next
                    if node.prev:
                        node.prev.next=node.next
                    if node.next:
                        node.next.prev=node.prev
                    self._tail.next=node
                    node.prev=self._tail
                    self._tail=node
                    node.next=None
            else:
                node=Node(key)
                self._tail.next=node
                node.prev=self._tail
                self._tail=node
                node.next=None
                self._lm[key]=node
                
                if len(self._m)>=self._cap:
                    rm=self._head
                    self._head=self._head.next
                    rm.next=None
                    self._head.prev=None
                    del self._m[rm.val]
                    del self._lm[rm.val]
        self._m[key]=value
