# Last updated: 18/12/2025, 20:19:42
class Node :
    def __init__(self, key = 0, value = 0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
# we have hashmap which will store the key and node for o(1) lookup
# we have doouble ended linked list to alway shifts most recently used towards the head which inturn moves least recently used towards the end.

class LRUCache:
    def __init__(self,capacity ):
        self.capacity = capacity
        self.cache = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
    def _remove_node(self, node):
        # unlink node

        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev
        return node
    def _add_to_head(self,node):
        nxt = self.head.next
        nxt .prev = node
        self.head.next = node
        node.prev = self.head
        node.next = nxt
    def _pop_tail(self):
        node = self._remove_node(self.tail.prev)
        return node
    def get(self, key: int) -> int:
        node = self.cache.get(key, None)
        if not node: 
            return -1
        self._remove_node(node)
        self._add_to_head(node)
        return node.value
    def put(self, key: int, value: int) -> None:
        node = self.cache.get(key)
        if node:
            node.value = value
            self._remove_node(node)
            self._add_to_head(node)
        else:
            new_node = Node(key,value)
            self.cache[key] = new_node
            self._add_to_head(new_node)
            self.size +=1
            if self.size > self.capacity:
                tail_node = self._pop_tail()
                del self.cache[tail_node.key]
                self.size -= 1



        


    
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)