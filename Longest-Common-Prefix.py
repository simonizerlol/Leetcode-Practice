# level: easy
# complexity: time o(n^2), space o(n^2)
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        """
        if input is empty, return ""
        find the max length the longest common prefix can be, which is the max length of the shorted string from the input
        """
        if len(strs) == 0 :
            return ""

        '''
        sorted(strs, key=len) sorts the strings by length, from shortest to longest.
        '''
        self.max_length = len(sorted(strs, key = len)[0])
        self.longest = ""

        '''
        iterate through index of each input string
        '''
        for i in range(self.max_length) :
            self.char_at_an_index = [word[i] for word in strs]
            '''
            count() returns the number of occurrences of a substring in the given string.
            '''
            if self.char_at_an_index.count(self.char_at_an_index[0]) == len(self.char_at_an_index) :
                self.longest += str(self.char_at_an_index[0])
            else :
                return self.longest
        return self.longest
