// 66. Plus One https://leetcode.com/problems/plus-one/
class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        // turns all trailing nines into zeros and if it comes across a non-nine, it increases that and returns
        for (int i = digits.size() - 1; i >= 0; --i){
            if (digits[i] == 9){
                digits[i] = 0;
            }
            else{
                digits[i]++;
                return digits;
            }
        }

        /* if the for-loop ended without returning, it means the array must have looked like [9,9,9], or [9,9,9,9] etc.
        Say the array was [9,9,9]. After the for-loop, it looks like [0,0,0] when it should look like [1,0,0,0].
        So changes the first zero with 1 and adds a zero at the end.
        */
        digits[0] = 1;
        digits.push_back(0);
        return digits;
    }
};
