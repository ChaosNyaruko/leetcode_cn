def _hash(key):
    return key % 769

class node:
    def __init__(self, key, value):
        self.key = key
        self.value = value 
        self.next = None

class MyHashMap:
    def __str__(self):
        res = ""
        for dummy in self.data:
            p = dummy.next
            while p:
                res += "{0}:{1} ".format(str(p.key), str(p.value))
                p = p.next
        res += "\n" 
        return res

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = [node(0, 0) for _ in range(769)]


    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        k = _hash(key)
        prev = self.data[k]
        p = prev.next
        while p and p.key != key:
            prev = p
            p = p.next

        if not p:
            prev.next = node(key, value)             
        else:
            assert(p.key == key)
            p.value = value

        # print(self)
        return

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        k = _hash(key)
        prev = self.data[k]
        p = prev.next
        while p:
            if p.key == key:
                return p.value 
            prev = p
            p = p.next
        return -1


    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        k = _hash(key)
        prev = self.data[k]
        p = prev.next
        while p:
            if p.key == key:
                prev.next = p.next
                return
            prev = p
            p = p.next

        return

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
if __name__ == '__main__':
    obj = MyHashMap()
    obj.put(1, 1)
    obj.put(2, 2)
    print(obj.get(1))

