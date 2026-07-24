//
// Created by Kotake on 2021/8/20.
//
#include "bits/stdc++.h"

class Solution {
public:
    int search(vector<int> &nums, int target) {
        int n = nums.size();
        if (n == 0)return -1;
        if (n == 1)return nums[0] == target ? 0 : -1;
        int l = 0, r = n - 1;
        while (l <= r) {
            int mid = (l + r) / 2;
            if (nums[mid] == target)return mid;
            if (nums[mid] >= nums[0]) {
                if (target >= nums[0] && target < nums[mid]) {
                    r = mid - 1;
                } else {
                    l = mid + 1;
                }
            } else {
                if (target > nums[mid] && target <= nums[n - 1]) {
                    l = mid + 1;
                } else {
                    r = mid - 1;
                }
            }
        }
        return -1;
    }
};

int main() {
    Solution sol;
    vector<int> a = {4, 5, 6, 7, 0, 1, 2};
    cout << sol.search(a, 0);
    return 0;
}