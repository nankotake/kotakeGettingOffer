//
// Created by Kotake on 2021/8/7.
//
#include <iostream>
#include <string>

using namespace std;

class Solution {
public:
    bool isAnagram(string s, string t) {
        int ss[26] = {0}, tt[26] = {0};
        if (s.size() != t.size())return false;
        for (int i = 0; i < s.size(); i++) {
            ss[s[i] - 'a']++;
            tt[t[i] - 'a']++;
        }
        for (int i = 0; i < 26; i++) {
            if (ss[i] != tt[i])return false;
        }
        return true;
    }
};

int main() {
    string s = "sss";
    string t = "ttt";
    Solution sol;
    cout << sol.isAnagram(s, t);
    return 0;
}
