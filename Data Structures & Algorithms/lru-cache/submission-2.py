class Node:
    def __init__(self, key, val):
        self.next = None
        self.prev = None
        self.key = key
        self.val = val

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.head = Node(0, 0)
        self.tail = Node(0 ,0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity

    def add(self, node):
        prev = self.head
        next = self.head.next
        prev.next = next.prev = node
        node.next, node.prev = next, prev
    
    def remove(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            print(node.key, node.val)
            self.remove(node)
            self.add(node)
            return node.val
        return -1


    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
        self.cache[key] = Node(key, value)
        self.add(self.cache[key])
        
        # if capacity
        if len(self.cache) > self.capacity:
            lru = self.tail.prev
            self.remove(lru)
            del self.cache[lru.key]
