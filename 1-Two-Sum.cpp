// # 1. Two Sum https://leetcode.com/problems/two-sum/
// # leve: easy
// # complexity:  Time O(n), Space: O(n)
// """
// Explaination:
// brute force would be checking each value in the list and the ones that follows, to see if they sum up to target value.
// The optimal solution is to use a hashmap
// """

// rewriting my python code in cpp to brush up my cpp
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int>map;

        for(int i = 0; i < nums.size(); i++){
            if(map.find(target-nums[i]) != map.end()){
               return {i, map[target - nums[i]]};
            }
            else{
                map[nums[i]] = i;
            }
        }
        return {};
    }
};
