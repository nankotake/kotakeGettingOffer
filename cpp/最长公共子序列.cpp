//
// Created by Kotake on 2021/8/31.
//
#include "bits/stdc++.h"
class Solution {
public:
    int longestCommonSubsequence(string text1, string text2) {
        int m=text1.size(),n=text2.size();
        vector<vector<int>> dp(m+1,vector<int>(n+1));
        for(int i=1;i<=m;i++){
            char mi=text1[i-1];
            for(int j=1;j<=n;j++){
                char nj=text2[j-1];
                if(mi==nj){
                    dp[i][j]=dp[i-1][j-1]+1;
                }
                else {
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1]);
                }
            }
        }
        return dp[m][n];
    }
};
int main(){
    string s1,s2;
    cin >> s1 >> s2;
    s1="123123123";
    s2="232323";
    Solution sol;
    cout << sol.longestCommonSubsequence(s1,s2);
    return 0;
}