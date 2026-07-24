//
// Created by Kotake on 2021/8/30.
//

#include "bits/stdc++.h"
int add(int a,int b){
    while(b!=0){
        int temp = (unsigned int)(a&b)<<1;
        a^=b;
        b=temp;
    }
    return a;
}
int main(){
    int a,b;cin >> a >> b;
    cout << add(a,b);
}