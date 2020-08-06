# 142 Linked List Cycle II https://leetcode.com/problems/linked-list-cycle-ii/
# level: medium

# similar approach as 287. Find the Duplicate Number https://leetcode.com/problems/find-the-duplicate-number/description/
"""
Explaination:
The idea is to have two pointers iterating through the list, with one pointer either ahead by a fixed amount or actually moving faster.
To determine if a linked list has a cycle, do the same thing where 1 pointer moves ahead 2 nodes at a time.
If there's a cycle, the runner will eventually equal the normal curr node. If not, will hit null node.
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = fast = head
        has_cycle = False
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                has_cycle = True
                break
        if not has_cycle:
            return None

        # the point where they meet again, resetting slow to head, is the cycle start
        while head != fast:
            head = head.next
            fast = fast.next
        return head
