# level: easy
# complexity: time O(n), space O(1)
# https://leetcode.com/problems/reverse-integer/
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # this is the almost 1 liner
        sign = cmp(x,0) # if x is greater than 0, then sign is 1, else -1
        reversed = int(str(x*sign)[::-1]) # covert possitive x to string, then reverse it, finally covert it back to int
        return sign*reversed * (r < 2**31)

        """
        traditional way:
        """
        # check if x is within the 32-bit signed integer range
        # if(x > ((2**31)-1) or x < -1 * (2**31)):
        #     return 0

        reversed = 0
        num = x
        x = abs(x)

        while(x > 0):
            reversed = reversed * 10 + x % 10
            x = x//10 # floor division

        # check if reversed integer overflows (is within the 32-bit signed integer range)
        if(reversed > ((2**31)-1) or reversed < -1 * (2**31)):
            return 0

        return reversed if(num > 0) else -1 * reversed
