//
// Created by Kotake on 2021/9/16.
//

#include "bits/stdc++.h"
class Solution {
public:
    pair<int,int> get(string s,int a,int b)
    {
        int i,j;
        for(i=a,j=b;i>=0 && j <s.size();i--,j++){
            if(s[i]!=s[j])return {i + 1, j - 1};
        }
        return {i+1,j-1};
    }
    string longestPalindrome(string s) {
        int a=0,b=0;
        for(int i=0;i<s.size();i++){
            auto l1=get(s,i,i);
            auto l2=get(s,i,i+1);
            if(l1.second-l1.first>b-a){a=l1.first;b=l1.second;}
            if(l2.second-l2.first>b-a){a=l2.first;b=l2.second;}

        }
        return s.substr(a,b-a+1);
    }
};
int main(){
    Solution sol;
    string s;
//    cin >> s;
    s="babad";
    cout << sol.longestPalindrome(s);
}