# 53. Maximum Subarray https://leetcode.com/problems/maximum-subarray/
# level: easy
# complexity: O(n) time, O(1) space

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        first implementation
        """
        sum = lowest_point = max_point = 0 # current sum and current lowest/max point
        M =  = -float("inf") # current Max sum set to -infinity

        for n in nums:
            sum += n
            M = max(M, sum-lowest_point)

            if(sum < lowest_point):
                lowest_point = sum
            elif(sum >= max_point):
                max_point = sum
        return M

        """
        Kadane’s Algorithm (Dynamic Programming) implementation
        If the sum of a subarray is positive, it has possible to make the next value bigger, so we keep do it until it turn to negative.
        If the sum is negative, it has no use to the next element, so we break.
        """
        for i in range(1, len(nums)):
            nums[i] = max(nums[i], nums[i-1] + nums[i])
        return max(nums)

        """
        Divide and conquer implementation, O(nlogn) time
        Since the master theorem says a = 2, b = 2, d = 1,
        thus, the complexity should ba case 1, which means nlogn.
        """
        def divide_and_conquer(nums, i, j):
            if i == j-1:
                return nums[i],nums[i],nums[i],nums[i]

            # we will compute :
            # a which is max contiguous sum in nums[i:j] including the first value
            # m which is max contiguous sum in nums[i:j] anywhere
            # b which is max contiguous sum in nums[i:j] including the last value
            # s which is the sum of all values in nums[i:j]

            # compute middle index to divide array in two halves
            index_mid = i+(j-i)//2

            # compute a, m, b, s for left half
            a1, m1, b1, s1 = divide_and_conquer(nums, i, index_mid)

            # compute a, m, b, s for right half
            a2, m2, b2, s2 = divide_and_conquer(nums, index_mid, j)

            # combine a, m, b, s values from left and right halves to form a, m, b, s for whole array (bottom up)
            a = max(a1, s1+a2)
            b = max(b2, s2+b1)
            m = max(m1,m2,b1+a2)
            s = s1+s2
            return a,m,b,s

        _,m,_,_ = divide_and_conquer(nums, 0, len(nums))
        return m
