# 1. Two Sum https://leetcode.com/problems/two-sum/
# leve: easy
# complexity:  Time O(n), Space: O(n)
"""
Explaination:
brute force would be checking each value in the list and the ones that follows, to see if they sum up to target value.
The optimal solution is to use a hashmap
"""

class Solution(object):
    def twoSum(self, nums, target):
        map_so_far = {} # val : index

        for index, value in enumerate(nums):
            diff = target - value
            if diff in map_so_far:
                return [map_so_far[diff], index] # since there is only 1 solution

            # if can't find the solution, then update the hashmap
            map_so_far[value] = index
        return # this "return" is optional
