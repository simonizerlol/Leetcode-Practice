# level: easy
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        tmp = ListNode
        '''
        edge cases, check if l1 is empty then return l2, since it's already sorted
        also check if l2 is empty then return l1
        '''
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        '''
        compare each value of the 2 linkedlist using recursion
        '''
        if l1.val < l2.val:
            tmp = l1
            l1.next = self.mergeTwoLists(l1.next, l2)
        else:
            tmp = l2
            l2.next = self.mergeTwoLists(l2.next, l1)

        return tmp
