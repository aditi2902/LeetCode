class Node:
    def __init__(self,key=0,value=0):
        self.key=key
        self.value=value
        self.next=None
        self.prev=None

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity=capacity
        self.cache={}

        self.head=Node()
        self.tail=Node()
        self.head.next=self.tail
        self.tail.prev=self.head

    def remove(self,node):
        prevn=node.prev
        nextn=node.next
        prevn.next=nextn
        nextn.prev=prevn

    def insert(self,node):
        prevn=self.tail.prev
        prevn.next=node
        node.prev=prevn
        node.next=self.tail
        self.tail.prev=node
        
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if not key in self.cache:
            return -1
        node=self.cache[key]
        self.remove(node)
        self.insert(node)
        return node.value


        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.cache:
            self.remove(self.cache[key])
        node=Node(key,value)
        self.insert(node)
        self.cache[key]=node
        if len(self.cache)>self.capacity:
            lru=self.head.next
            self.remove(lru)
            del self.cache[lru.key]

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)