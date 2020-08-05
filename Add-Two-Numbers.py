# 2. Add Two Numbers https://leetcode.com/problems/add-two-numbers/
# level: medium
# complexity: O(n) time and space

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        root = n = ListNode(0)
        while l1 or l2 or carry:
            v1 = v2 = 0
            if l1: # to make sure that the node isn't None
                carry += l1.val
                l1 = l1.next
            if l2: # to make sure that the node isn't None
                carry += l2.val
                l2 = l2.next
            carry, val = divmod(carry, 10) # returns a pair of numbers (a tuple) consisting of their quotient and remainder.
                                           # example: divmod(8, 10) =  (0, 8)

            # At the start, both root and n are assigned to point towards the same ListNode.
            # This same ListNode is updated in the while loop via n,
            # and in the end we refer to the start of the ListNode (but skipping the head)
            # using root.next.
            # We use root.next instead of root to skip the dummy head of value 0.

            n.next = n = ListNode(val) #  first n.next = ListNode(val) then n point to the same address
        return root.next
