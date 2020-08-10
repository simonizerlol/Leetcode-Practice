// # 14. Longest Common Prefix https://leetcode.com/problems/longest-common-prefix/
// # level: easy
// # complexity: time complexity is O(min_length * n), where min_length is the minimum length of the strs and n is the number of strs.
// #             space: O(1) constant space

// rewriting my python code in cpp to brush up my cpp
class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
      string lcp = "";
      if(strs.empty()) return lcp;

      sort(strs.begin(), strs.end());
      string minLength = strs.front();
      string maxLength = strs.back();

      for(int i = 0; i < minLength.size(); i++){
          if(minLength[i] == maxLength[i])
              lcp += minLength[i];
          else
              break;
      }
      return lcp;
    }
};
