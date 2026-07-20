//
// Created by Administrator on 2021/10/12.
//

#include "bits/stdc++.h"
class Solution {
private:
    unordered_map<int, vector<string>> ans;
    unordered_set<string> wordSet;

public:
    vector<string> wordBreak(string s, vector<string>& wordDict) {
        wordSet = unordered_set<string>(wordDict.begin(), wordDict.end());
        backtrack(s, 0);
        return ans[0];
    }

    void backtrack(const string& s, int index) {
        if (!ans.count(index)) {
            if (index == s.size()) {
                ans[index] = {""};
                return;
            }
            ans[index] = {};
            for (int i = index + 1; i <= s.size(); ++i) {
                string word = s.substr(index, i - index);
                if (wordSet.count(word)) {
                    backtrack(s, i);
                    for (const string& succ: ans[i]) {
                        ans[index].push_back(succ.empty() ? word : (word + " " + succ));
                    }
                }
            }
        }
    }
};
int main(){
    string a="catsanddog";
    vector<string> d={"cat","cats","and","sand","dog"};
    Solution sol;
    vector<string> ans=sol.wordBreak(a,d);
    for(string i : ans)cout << i << endl;
    return 0;
}