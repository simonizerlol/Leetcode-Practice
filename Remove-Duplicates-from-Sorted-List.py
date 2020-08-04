# level: easy
# complexity: O(n) time and space, takes n time to iterate through the list

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        """
        iterative implementation: given a sorted linked list, we can just go through the linked list, and see if there's any duplicate node
        """
        cur = head
        while cur and cur.next:
            if cur.val == cur.next.val:
                cur.next = cur.next.next   # skip duplicated node
            else:
                cur = cur.next  # no duplicate, move to next node

        return head

        """
        recursion implementation
        complexity: O(n) time and space
        """
        if head and head.next:
            head.next = self.deleteDuplicates(head.next)
            return head.next if head.next.val == head.val else head # move on to the next node after head.next if duplicate exists, else dont
        return head
