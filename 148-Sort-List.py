# 148. Sort List https://leetcode.com/problems/sort-list/description/
# level: medium

# Similar to Leetcode: 21. Merge Two Sorted Lists #
# Similar to Leetcode: 876. Middle of the Linked List #
"""
The problem asks to sort in O(nlogn) time and O(1) space complexity
My initial instinct is to divide and conquer, implement one of the sorting algorthms.

The idea is to have two pointers iterating through the list,
with one pointer either ahead by a fixed amount or actually moving faster.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        """
        recursive implementation:

        Explaination:
        Each time divided the given list into two sub list.
        Then merge sub list after bottom case return.

        Note. since it's a recursion, it's is O(n) space complexity unfortunately, since you store log(n) calls in stack.
        """
        # base case: as we branch and move left, left ... when only one node is left, we return it
        if not head or not head.next:
            return head

        # get middle (if even, get 1st middle)
        slow = head
        fast = head.next # for [1,2,3,4] as mid will be node 3, if this statement not used
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # split list in two and sort halves
        h2 = slow.next # slow is at middle, next elements are considered right

        # cut down the first part
        slow.next = None # this makes left has only left part
        left = self.sortList(head)
        right = self.sortList(h2)
        # then merge sorted halves
        return self.merge_sortedList(left, right)

    def merge_sortedList(self, h1, h2):
        if not h1 or not h2:
            return h1 or h2

        if h1.val <= h2.val:
            h1.next = self.merge_sortedList(h1.next, h2)
            return h1
        else:
            h2.next = self.merge_sortedList(h1, h2.next)
            return h2

        """
        In order to get O(1) space complexity, we need to perform a bottom-up without using stack.
        """
        # base case: as we branch and move left, left ... when only one node is left, we return it
        if not head or not head.next:
            return head

        slow, fast, pre = head, head, None

        while fast and fast.next:
            slow, fast, pre = slow.next, fast.next.next, slow

        pre.next = None
        left, right = self.sortList(head), self.sortList(slow)
        dum = ListNode(0)
        p = dum

        while left or right:
            if not left:
                p.next = right
                right = right.next
            elif not right:
                p.next = left
                left = left.next
            else:
                if left.val > right.val:
                    p.next = right
                    right = right.next
                else:
                    p.next = left
                    left = left.next
            p = p.next
        return dum.next
