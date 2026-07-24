//
// Created by Kotake on 2021/8/22.
//
#include "bits/stdc++.h"

class Solution {
public:
    bool isStraight(vector<int> &nums) {
        sort(nums.begin(), nums.end());
        int count = 0;
        int target = 0;
        int flag = true;
        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] == 0) {
                count++;
                target++;
                continue;
            }
            if (i > target && nums[i] - nums[i - 1] != 1) {
                if (nums[i] - nums[i - 1] > count + 1 || nums[i] == nums[i-1]) { return false; }
                else {
                    count = count - (nums[i] - nums[i - 1] - 1);
                    i += nums[i] - nums[i - 1] - 2;
                }
            }
        }
        return flag;
    }
};

int main() {
    vector<int> a = {0,0,2,2,5};
    Solution solution;
    cout << solution.isStraight(a);
    return 0;
}