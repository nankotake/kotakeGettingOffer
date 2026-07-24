//
// Created by Kotake on 2021/8/21.
//
/*
 * 找数组里两个数相加比M小的组合数，可以重复
 *
*/

#include "bits/stdc++.h"
using namespace std;
int atoi(string i){
    int rel = 0;
    bool flag=true;
    if(i[0]=='-') {
        flag = false;
        i[0]='0';
    }
    for(char j : i){
        rel = rel*10 + j - '0';
    }
    return flag?rel:(0-rel);
}
int main(){
    char temp;
    string t;
    vector<int> m;int M;
    int rel=0;
    while(temp=getchar()){
        if(temp==' '){
            m.push_back(atoi(t));
            t.clear();
        }
        else if (temp=='\n'){
            if(!t.empty())
                m.push_back(atoi(t));
            break;
        }
        else {
            t = t + temp;
        }
    }
    cin >> t;M=atoi(t);
    sort(m.begin(),m.end());
    int size=m.size();
    for(int i=0;i<size;i++){
        for(int j=i+1;j<size;j++){
            if(m[i]+m[j]<M)rel++;
            else size=j;
        }
    }
//    if(rel>0)
        cout << rel;
    return 0;
}