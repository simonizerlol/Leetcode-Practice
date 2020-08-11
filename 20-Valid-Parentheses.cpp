// 20. Valid Parentheses https://leetcode.com/problems/valid-parentheses/
// complexity: O(n) time as traversing the given string one character at a time and push, and pop operations on a stack take O(1) time
//              O(n) space as pushing all opening brackets onto the stack and in the worst case, we will end up pushing all the brackets onto the stack. e.g. ((((.

class Solution {
public:
    bool isValid(string s) {
      stack<char> stk;
      // auto prevents accidental type conversions, it automatically decides the type of the variable at compile time.
      for(const auto c : s){
          switch(c){
              case '{':  stk.push('}'); break;
              case '[':  stk.push(']'); break;
              case '(':  stk.push(')'); break;
              default:
                  if(stk.empty() || c != stk.top()) return false;
                  else stk.pop();
          }
      }
      return stk.empty();
    }
};
