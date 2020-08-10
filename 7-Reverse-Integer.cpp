// # 7. Reverse Integer https://leetcode.com/problems/reverse-integer/
// # level: easy
// # complexity: time O(log(x)) as there are about log x digits in x, space O(1)

// rewriting my python code in cpp to brush up my cpp
class Solution {
public:
    int reverse(int x) {
        // The idea is to repeatedly pop the last digit off of x and push it to the back of the rev.
        long rev = 0;
        while(x){
            rev = rev*10 + x%10;
            x /= 10; // x = x/10;
        }
        // check and see if reversed integer overflows.
        if(INT_MAX < rev || INT_MIN > rev){
            return 0;
        }
        else{
            return rev;
        }
    }
};
