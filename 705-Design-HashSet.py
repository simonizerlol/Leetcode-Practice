# 705. Design HashSet https://leetcode.com/problems/design-hashset/
# level: easy
# complexity:

# Design a HashSet without using any built-in hash table libraries.
class MyHashSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.h = []

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        if key not in self.h:
            self.h.append(key)


    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        if key not in self.h:
            return False
        else:
            self.h.remove(key)
            return True

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        if key in self.h:
            return True
        else:
            return False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)

    """
    This problem can also be thought differently, as demonstrated below, though not space efficient
    """
    def __init__(self):
        self.h = [False] * 1000000 # given the condition of all values will be in the range of [0, 1000000].

    def add(self, key):
        self.h[key] = True

    def remove(self, key):
        self.h[key] = False

    def contains(self, key):
        return self.h[key]
