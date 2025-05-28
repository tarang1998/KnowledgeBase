
class Node:
    def __init__(self,key,value):
        self.prev = None
        self.next = None 
        self.key = key
        self.value = value

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity 
        self.cache = {}

        self.lru = Node(None, None)
        self.mru = Node(None, None)

        self.lru.next = self.mru
        self.mru.prev = self.lru
    

    # Helper functions
    def insert(self,node):
        prev = self.mru.prev
        prev.next = node

        node.prev = prev
        node.next = self.mru
        self.mru.prev = node

        
    def remove(self,node):
        prev = node.prev
        next = node.next 
        prev.next = next 
        next.prev = prev

        node.next = None
        node.prev = None
        

    def get(self, key: int) -> int:

        if key in self.cache:
            node= self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.value
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:

        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.remove(node)
            self.insert(node)
            
        else:

            node = Node(key,value)
            self.cache[key] = node
            self.insert(node)

            if len(self.cache) > self.capacity:
                node = self.lru.next
                self.remove(node)
                del self.cache[node.key]



      
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)









###############################################################

class Node:
    def __init__(self,key,value):
        self.prev = None
        self.next = None 
        self.key = key
        self.value = value

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity 
        self.lru = None
        self.mru = None
        self.cache = {}
     
        

    def get(self, key: int) -> int:
        print("get")

        if key in self.cache:
            node = self.cache[key]


            if node == self.mru:
                return node.value 

            elif node == self.lru:
                nextNode = node.next
                nextNode.prev = None
                node.next = None
                self.lru = nextNode
                
                temp = self.mru
                temp.next = node
                node.prev = temp
                self.mru = node
            else:

                temp = node
                nextNode = node.next
                prevNode = node.prev
                prevNode.next = nextNode
                nextNode.prev = prevNode
                
                temp = self.mru 
                node.next = None 
                node.prev = temp
                temp.next = node
                self.mru = node
            
            return node.value
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:

        if key in self.cache:
            node = self.cache[key]
            node.value = value
            
            if node == self.mru:
                pass
            elif node == self.lru:
                nextNode = node.next
                nextNode.prev = None
                node.next = None
                self.lru = nextNode
                
                temp = self.mru
                temp.next = node
                node.prev = temp
                self.mru = node
            else:
                temp = node
                nextNode = node.next
                prevNode = node.prev
                prevNode.next = nextNode
                nextNode.prev = prevNode
                
                temp = self.mru 
                node.next = None 
                node.prev = temp
                temp.next = node
                self.mru = node
        else:
            node = Node(key,value)

            self.cache[key] = node

            if self.lru == None and self.mru == None:
                self.lru = node
                self.mru = node
            else:
                temp = self.mru 
                temp.next = node 
                node.prev = temp
                self.mru = node

            if len(self.cache) > self.capacity:
                temp = self.lru 
                del self.cache[temp.key]
                nextNode = temp.next
                nextNode.prev = None 
                self.lru = nextNode

        print("put")


      
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)