// 70. Climbing Stairs https://leetcode.com/problems/climbing-stairs/
// level: easy
// complexicity:

class Solution {
public:
    int climbStairs(int n) {
        // this problem can be solved several ways including 1) brute force, 2) recrusion+memoization, 3) dynamic programming, 4) fibonacci number, and two other approach which i am unfamiliar with, Binets Method and Fibnonacci Formula.

        // recrusive + memoization (top-down) implementation:
        // complexicity: O(n) time as n is size of recursion tree can go upto.
        //               O(n) space as n is the depth of recursion tree can go upto.
        vector<int> memo(n+1,0);
        return climb(n, memo);

        // fibonacci number implementation: https://www.youtube.com/watch?v=wTlw7fNcO-0
        // complexicity: O(n) time as single loop upto n is required to calculate n^th  fibonacci number.
        //               O(1) space
        if (n == 1) return 1;
        int first = 1;
        int second = 2;
        for (int i = 3; i <= n; i++) {
            int third = first + second;
            first = second;
            second = third;
        }
        return second;
    }

    int climb(int n, vector<int> &memo){
        if(n == 1 || n == 2) return n;

        if(memo[n] > 0) {
            return memo[n];
        }
        
        int result = climb(n-1, memo)+climb(n-2, memo);
        memo[n] = result;
        return result;
    }
};
