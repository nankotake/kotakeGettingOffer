//
// Created by Kotake on 2021/8/3.
//
#include <vector>
#include <iostream>

using namespace std;

class Solution {
public:
    int maxArea(vector<int> &height) {
        int left = 0, right = height.size() - 1;
        int m = 0;
        while (left < right) {
            int ll = height[left], rr = height[right];
            int temp = (right - left) * min(ll, rr);
            m = max(m, temp);
            if (ll < rr)left++;
            else right--;
        }
        return m;
    }
};

int main() {
    Solution sol;
    vector<int> input = {1, 8, 6, 2, 5, 4, 8, 3, 7};
    cout << sol.maxArea(input);
    return 0;
};