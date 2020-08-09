# 706. Design HashMap https://leetcode.com/problems/design-hashmap/
# level: easy
# complexity:

# Design a HashMap without using any built-in hash table libraries.
class MyHashMap(object):
    """
    a simple implementation to start with
    """
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.h = [-1]*1000001 # given all keys and values will be in the range of [0, 1000000].

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: None
        """
        self.h[key] = value

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        return self.h[key]


    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: None
        """
        self.h[key] = -1
        
    """
    Open hashing approach: TODO
    reference https://leetcode.com/problems/design-hashmap/discuss/185347/Hash-with-Chaining-Python
    """

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
