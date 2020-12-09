#
# @lc app=leetcode.cn id=146 lang=python3
#
# [146] LRU 缓存机制
#

# @lc code=start
class DLinkedList:
    def __init__(self, key = 0, value = 0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.head = DLinkedList()
        self.tail = DLinkedList()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.record = dict()


    def get(self, key: int) -> int:
        if key not in self.record:
            return -1
        node = self.record[key]
        self.move_to_head(node)
        return node.value


    def put(self, key: int, value: int) -> None:
        if key not in self.record:
            node = DLinkedList(key = key, value = value)
            self.add_to_head(node)
            self.size += 1
            self.record[key] = node
            if self.size > self.capacity:
                removed = self.remove_tail_node()
                self.size -= 1
                self.record.pop(removed.key)
        else:
            node = self.record[key]
            node.value = value
            self.move_to_head(node)
    def remove_node(self, node):
        node.prev.next =  node.next
        node.next.prev = node.prev
        node.prev = None
        node.next = None

    def move_to_head(self, node: 'DLinkedList'):
        self.remove_node(node)
        self.add_to_head(node) 
        
    def add_to_head(self, node: 'DLinkedList'):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
    def remove_tail_node(self) -> 'DlinkedList':
        node = self.tail.prev
        self.remove_node(node)
        return node 





# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

