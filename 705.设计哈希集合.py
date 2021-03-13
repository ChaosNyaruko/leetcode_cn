class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.set_ = [-1] * int(1e6 + 1)

    def add(self, key: int) -> None:
        self.set_[key] = 0


    def remove(self, key: int) -> None:
        self.set_[key] = -1

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        return self.set_[key] != -1
