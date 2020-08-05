# 3. Longest Substring Without Repeating Characters https://leetcode.com/problems/longest-substring-without-repeating-characters/
# level: medium
"""
complexity: Time complexity :O(n).
n is the length of the input string.
It will iterate n times to get the result.

Space complexity: O(m)
m is the number of unique characters of the input.
We need a dictionary to store unique characters.
"""
# when you see "substring", it's a sliding window problem
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        """
        built-in function enumerate example:
        str = "Pig"
        for index, char in enumerate(str):
            print index, char

        # Output:
        # 0 P
        # 1 i
        # 2 g
        """
        seen, res, start, = {}, 0, 0 # using dictionary/hashmap, the lookup time is O(1)
        for index, char in enumerate(s):
            # when char already in dictionary
            if char in seen:
                # check length from start of string to index and update the res
                # move the pointer when a repeated character is seen
                res = max(res, index-start)

                # update start of string index to the next index
                start = max(start, seen[char]+1)

            # add/update char to/of dictionary
            seen[char] = index

        # answer is either in the begining/middle OR some mid to the end of string
        # return should consider the last non-repeated substring
        return max(res, len(s)-start)


        """
        Another sliding window implementation:
        All characters inside this window are unique.
        Window border is [left + 1, right] and window size is right - left.
        """
        last_index, result, left = {}, 0, -1
        for right, char in enumerate(s):
            left = max(left, last_index.get(char, -1))
            last_index[char] = right
            result = max(result, right - left)
        return result
