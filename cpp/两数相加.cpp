//
// Created by Kotake on 2021/8/7.
//
#include <iostream>
#include <unordered_map>
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int> &nums, int target) {
        unordered_map<int, int> mp;
        //建立哈希表
        for (int i = 0; i < nums.size(); i++) {
            mp[nums[i]] = i;
        }
        //遍历哈希表
        for (int i = 0; i < nums.size(); i++) {
            //目标值target-nums[i]在哈希表中存在，且不为当前值(目标元素不能是自身，即mp中所找到的对应元素的下标不等于当前元素下标i)
            if (mp.find(target - nums[i]) != mp.end() && mp[target - nums[i]] != i) {
                return {i, mp[target - nums[i]]};
            }
        }
        return {};
    }
};

int main() {
    vector<int> v = {2, 5, 3, 7, 1};
    Solution sol;
    v = sol.twoSum(v, 9);
    cout << v[0] << ' ' << v[1];
    return 0;
}