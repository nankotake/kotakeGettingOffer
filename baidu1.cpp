//
// Created by Kotake on 2021/9/7.
//

#include <iostream>
#include <vector>
#include <string>
using namespace std;
int main(){
    string s1;cin >>s1;
    int now=0;
    int count=0;
    for(char i : s1){
        if(now==0 && i=='E' || i=='e')now++;
        else if(now==1 && i=='a' || i=='A')now++;
        else if(now==2&&i=='S'|i=='s')now++;
        else if(now==3&&i=='y'||i=='Y'){now=0;count++;}
    }
    cout << count;
    return 0;
}