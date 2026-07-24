//
// Created by Kotake on 2021/8/31.
//

#include "bits/stdc++.h"
class Solution{
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        priority_queue<pair<int,int>> pqueue;
        vector<int> rel;
        if(k>=nums.size()){
            int m=INT_MIN;
            for(int i : nums){
                m=max(i,m);
            }rel.emplace_back(m);return rel;
        }
        for(int i=0;i<k;i++){
            pqueue.push(pair<int,int>(nums[i],i));
        }
        rel.emplace_back(pqueue.top().first);
        for(int i=k;i<nums.size();i++){
            while(!pqueue.empty() && pqueue.top().second<=i-k){
                pqueue.pop();
            }
            pqueue.push(pair<int,int>(nums[i],i));
            rel.emplace_back(pqueue.top().first);
        }
        return rel;
    }
};
int main(){
    vector<int> a={1,-1};
    int k=1;
    Solution sol;
    vector<int> rel = sol.maxSlidingWindow(a,k);
    for(int i : rel){
        cout << i << ' ';
    }
    cout << endl;
    return 0;
}