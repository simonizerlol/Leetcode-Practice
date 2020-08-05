# 13. Roman to Integer https://leetcode.com/problems/roman-to-integer/
# level: easy
# complexity: O(n) time, O(1) space, where n is len(s)
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {
        "I":1,
        "V":5,
        "X":10,
        "L":50,
        "C":100,
        "D":500,
        "M":1000}
        """
        going backward implementation:
        >>> s='IV'
        >>> s[::-1]
        output 'VI'

        Explaination:
        Adding each letter back to front as result.
        unless something smaller is in front of something larger, in which case a subtraction instead of addition happens.
        """
        result, p = 0, 'I'
        for c in s[::-1]:
            result, p = result - d[c] if d[c] < d[p] else result + d[c], c
        return result

        """
        going forward implementation:

        Explaination:
        First sum up all single roman numerals,
        then if we find currValue > prevValue, we subtract 2 * prevValue,
        e.g. CM, first we get 1100, then we subtract 200, the result is 900.
        """
        prevValue, result = None, 0
        for c in s:
            currValue = d[c]
            result += currValue
            if prevValue and currValue > prevValue:
                result -= 2 * prevValue
            prevValue = currValue
        return result
