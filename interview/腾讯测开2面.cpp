//
// Created by Kotake on 2021/9/1.
//

#include "bits/stdc++.h"
class Solution{
public:
    vector<int> zhishu(int n){
        vector<int> rel;
        if(n<1)return rel;
        for(int i=1;i<n;i++){
            if(i==1 || i==2 || i==3) {
                rel.emplace_back(i);
                continue;
            }
            if(i%2==0 || i%3==0)continue;
            int j=2;
            bool flag=true;
            for(;j<=i/2;j++){
                if(i%j==0) {
                    flag=false;
                    break;
                }
            }
            if(flag)rel.emplace_back(i);
        }
        return rel;
    }
};
int main(){
    Solution sol;
    int N;cin >> N;
    vector<int> v=sol.zhishu(N);
    for(int i : v)cout << i << ' ';
    return 0;
}