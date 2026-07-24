//
// Created by Kotake on 2021/8/30.
//

/*
 * 一个长度大小为n的数组，数组中的每个元素的取值范围在[1,n]，且为正整数。
 * 问：如何在时间复杂度为O(n)，空间复杂度为O(1)的条件下，统计数组中不同元素出现的次数。
*/
#include "bits/stdc++.h"

void work(vector<int> &v){
    for(int i=0;i<v.size();i++){
        int temp = v[i] -1;
        if(temp<0){
            i++;
            continue;
        }
        if(v[temp]>0){
            v[i] = v[temp];
            v[temp] = -1;
        }
        else {
            v[temp]--;
            v[i]=0;
        }
    }
}

int main() {
    int N;
    cin >> N;
    vector<int> v;
    for (int i = 0; i < N; i++) {
        int temp;
        cin >> temp;
        v.push_back(temp);
    }
    work(v);
    for(int i=0;i<N;i++){
        if(v[i]<0){
            cout << i+1 << " : " << (-v[i]) << endl;
        }
    }
    return 0;
}