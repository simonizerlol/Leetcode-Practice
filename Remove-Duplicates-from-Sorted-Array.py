# 26. Remove Duplicates from Sorted Array https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# level: easy
# complexity: O(n) time, O(1) space
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # base case:
        if not nums:
            return 0

        # otherwise, length = 1, which is the length of the sorted array without duplicates.
        length = 1
        lst = nums[0]

        for n in nums:
            # if n is not a duplicate, then update length
            if n != lst:
                lst = n
                nums[length] = n
                length +=1
        nums = nums[:length]
        return length
