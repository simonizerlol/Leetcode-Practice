// # 13. Roman to Integer https://leetcode.com/problems/roman-to-integer/
// # level: easy
// # complexity: O(n) time, O(1) space, where n is len(s)

// rewriting my python code in cpp to brush up my cpp
class Solution {
public:
    int romanToInt(string s) {
      if (s.empty()) return 0; // check if the string is empty before use s.back()

      unordered_map<char, int> table = { { 'I' , 1 },
                                   { 'V' , 5 },
                                   { 'X' , 10 },
                                   { 'L' , 50 },
                                   { 'C' , 100 },
                                   { 'D' , 500 },
                                   { 'M' , 1000 } };
       int sum = 0;
       for (int i = 0; i < s.length(); ++i) {
           if (table[s[i]] < table[s[i + 1]]) {
               sum -= table[s[i]];
           } else {
               sum += table[s[i]];
           }
       }
       return sum;
    }
};
