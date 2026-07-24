//
// Created by Kotake on 2021/8/31.
//
#include "bits/stdc++.h"
class Solution{
public:
    vector<pair<char,int>> sol(string s){
        unordered_map<char,int> um;
        vector<char> rel;
        vector<pair<char,int>> r;
        for(char i : s){
            if(um.find(i)!=um.end()){
                um[i]++;
            }
            else{
                um[i]=1;
                rel.push_back(i);
            }
        }
        for(char i : rel){
            pair<char,int> p;
            p.first = i;
            p.second = um[i];
            r.emplace_back(p);
        }
        return r;
    }
    bool test(string s,vector<pair<char,int>> expected){
        vector<pair<char,int>> result = sol(s);
        if(result.size()!=expected.size())return false;
        for(int i=0;i<result.size();i++){
            if(result[i].first!=expected[i].first || result[i].second!=expected[i].second)return false;
        }
        return true;
    }
};
int main(){
    Solution sol;
    vector<string> ss = {
            ""," ","abc","aaa","\"",";drop","aaaaaaasdasdasdasdasdad","NULL","0x12312344","asd   asd"，"AAaasdSD"
    };
    vector<vector<pair<char,int>>> exps;
    vector<pair<char,int>> temp;

//    temp.emplace_back(pair<char,int>());
    exps.emplace_back(temp);
    temp.clear();

    temp.emplace_back(pair<char,int>(' ',1));
    exps.emplace_back(temp);
    temp.clear();

    temp.emplace_back(pair<char,int>('a',1));
    temp.emplace_back(pair<char,int>('b',1));
    temp.emplace_back(pair<char,int>('c',1));
    exps.emplace_back(temp);
    temp.clear();

    temp.emplace_back(pair<char,int>());
    exps.emplace_back(temp);
    temp.clear();

    for(int i=0;i<3;i++){
        cout << sol.test(ss[i],exps[i]) << endl;
    }

    return 0;
}
