# 198. House Robber https://leetcode.com/problems/house-robber/description/
# level: easy
# complexity: O(1) time and space

# dynamic programming
"""
Explaination:
Given an array, for each optimal value end of j is dp[j],
Then the recursive relation is: for new added j element, it has no border with dp[j-2], so dp[j-2]+ nums[j] is a candidate;
And at same time, it could be smaller than dp[j-1], which could have adjacent element with nums[j],
so the optimal value is max(max((dp[i-2]+nums[i]),dp[i-1]))

Based on the recursive formula:
    # Base Case: nums[0] = nums[0]
    # nums[1] = max(nums[0], nums[1])
    # nums[k] = max(k + nums[k-2], nums[k-1])
"""
# reference: https://leetcode.com/problems/house-robber/discuss/156523/From-good-to-great.-How-to-approach-most-of-DP-problems
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        # first attempt: Construct a dp table (Recursive (top-down))
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        dp = {}
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])

        return dp[len(nums)-1]

        """
        # second implementation: Constant space use two variables and compute the max respectively (Iterative + 2 variables (bottom-up))
        """
        prev1 = prev2 = 0
        for n in nums:
            prev1, prev2 = max(prev2 + n, prev1), prev1
        return prev1
