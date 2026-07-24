//
// Created by Kotake on 2021/8/22.
//
#include "bits/stdc++.h"
class Solution{
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        sort(nums.begin(),nums.end());
        vector<vector<int> > res;
        if(nums.size()<4)
            return res;
        int a,b,c,d,_size=nums.size();
        for(a=0;a<=_size-4;a++){
            if(a>0&&nums[a]==nums[a-1]) continue;      //确保nums[a] 改变了
            for(b=a+1;b<=_size-3;b++){
                if(b>a+1&&nums[b]==nums[b-1])continue;   //确保nums[b] 改变了
                c=b+1,d=_size-1;
                while(c<d){
                    if(nums[a]+nums[b]+nums[c]+nums[d]<target)
                        c++;
                    else if(nums[a]+nums[b]+nums[c]+nums[d]>target)
                        d--;
                    else{
                        res.push_back({nums[a],nums[b],nums[c],nums[d]});
                        while(c<d&&nums[c+1]==nums[c])      //确保nums[c] 改变了
                            c++;
                        while(c<d&&nums[d-1]==nums[d])      //确保nums[d] 改变了
                            d--;
                        c++;
                        d--;
                    }
                }
            }
        }
        return res;
    }
};

int main(){
    vector<int> a={2,2,2,2,2};
    int target = 8;
    vector<vector<int>> rel;
    Solution sol;
    rel = sol.fourSum(a,target);
    for(auto i : rel){
        for(auto j : i){
            cout << j << " ";
        }
        cout << endl;
    }
    return 0;
}