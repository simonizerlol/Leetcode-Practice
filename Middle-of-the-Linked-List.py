# 876. Middle of the Linked List https://leetcode.com/problems/middle-of-the-linked-list/
# level: easy
# complexity:

# Similar to Leetcode: 21. Merge Two Sorted Lists #
# Similar to Leetcode: 148. Sort List #

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # base case: as we branch and move left, left ... when only one node is left, we return it
        if not head or not head.next:
            return head

        """
        Each time, slow go 1 steps while fast go 2 steps.
        When fast arrives at the end, slow will arrive right in the middle.
        """
        # get middle (if even, get 1st middle)
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
