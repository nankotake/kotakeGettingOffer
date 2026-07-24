//
// Created by Kotake on 2021/9/16.
//

#include "bits/stdc++.h"
class Solution {
public:
    string addStrings(string num1, string num2) {
        int n1,n2;
        int flag=0;
        string rel;
        int N1=num1.size(),N2=num2.size();
        if(N1==0 || (N1==1&&num1[0]=='0'))return num2;
        if(N2==0 || (N2==1&&num2[0]=='0'))return num1;
        N1--;N2--;
        while(N1>=0 || N2>=0){
            if(N1>=0) n1=num1[N1]-'0';
            else n1=0;
            if(N2>=0) n2=num2[N2]-'0';
            else n2=0;
            rel=char((n1+n2+flag)%10+'0')+rel;
            if(n1+n2+flag>=10){
                flag=1;
            }else flag=0;
            N1--;N2--;
        }
        if(flag==1)rel='1'+rel;
        return rel;
    }
};
int main(){
    Solution sol;
    string a,b;
//    cin >> a >> b;
    a="11";b="123";
    cout << sol.addStrings(a,b);
    return 0;
}