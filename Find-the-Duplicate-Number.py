# 287. Find the Duplicate Number https://leetcode.com/problems/find-the-duplicate-number/description/
# level: medium
# complexity: it's O(n) time because we potentially can traverse all list.
#             it's O(1) space because we actually do not use any extra space: our linked list is virtual.

# similar approach as #142 Linked List Cycle II https://leetcode.com/problems/linked-list-cycle-ii/
"""
Explaination:
The idea is to have two pointers iterating through the list, with one pointer either ahead by a fixed amount or actually moving faster.
To determine if a linked list has a duplicate, do the same thing where 1 pointer moves ahead 2 nodes at a time.
If there's a duplicate, the runner will eventually equal the normal curr node. If not, will hit null node.
"""
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow = fast = duplicate = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        while duplicate != slow:
            slow = nums[slow]
            duplicate = nums[duplicate]
        return duplicate

        """
        another implementation: (similar)
        """
        slow = fast = duplicate = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        # Start up another pointer from the beginning of the array and iterate through the array
        # until it hits the pointer inside the array.
        while True:
            slow = nums[slow]
            duplicate = nums[duplicate]

            # If the two hit, the intersection index is the duplicate element.
            if slow == duplicate:
                return slow
