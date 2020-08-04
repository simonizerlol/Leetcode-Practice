# level: easy
# complexity: time complexity is O(min_length * n), where min_length is the minimum length of the strs and n is the number of strs.
#             space: O(1) constant space
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        """
        if input is empty, return ""
        find the max length the longest common prefix can be, which is the max length of the shorted string from the input
        can also be written as:
        if not strs:
            return ""
        """
        if len(strs) == 0 :
            return ""

        '''
        find the shortest string from strs, it determines when to end the iteration
        '''
        min_length = min(len(s) for s in strs) #n
        lcp = "" #lonngest common prefix

        '''
        iterate through index of each input string
        '''
        for i in range(min_length) : #m
            char_at_an_index = [word[i] for word in strs]
            '''
            count() returns the number of occurrences of a substring in the given string.
            '''
            if char_at_an_index.count(char_at_an_index[0]) == len(char_at_an_index) :
                lcp += str(char_at_an_index[0])
            else :
                return lcp
        return lcp
