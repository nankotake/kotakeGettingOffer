//
// Created by Kotake on 2021/8/7.
//
#include <iostream>
#include <string>

using namespace std;

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        if (s.size() == 0)return 0;
        int m[256] = {0}, l = 0, r = 0;
        int big = 0;
        while (r < s.size()) {
            if (m[s[r]] == 0 || m[s[r]] < l) {
                big = big > (r - l + 1) ? big : (r - l + 1);
            } else {
                l = m[s[r]];
            }
            m[s[r]] = r + 1;
            r++;
        }
        return big;
    }
};

int main() {
    Solution sol;
    cout << sol.lengthOfLongestSubstring("asdasdddsaaasadfgh");
    return 0;
}