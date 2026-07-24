//
// Created by Kotake on 2021/8/7.
//

#include <iostream>
#include <string>
using namespace std;

class Solution {
public:
    bool isNum(int i){return i<='9'&&i>='0';}
    int myAtoi(string s) {
        int rel=0;
        int i=0;
        int isM=0;
        while(s[i]==' '&&i<s.size())i++;
        for(;i<s.size();i++){
            if(s[i]<='9'&&s[i]>='0'){
                rel=rel*10+s[i]-'0';
            }
            else if(s[i]=='-' && isM==0){
                isM=1;
            }

        }
        if(isM==1){rel=0-rel;}
        return rel;
    };
    string myItoa(int i){
        string rel="";
        bool isM=false;
        if(i<0) {
            isM = true;
            i=0-i;
        }
        if(i==0)return "0";
        while(i!=0){
            rel = char(i%10+'0')+rel;
            i/=10;
        }
        if(isM)rel="-"+rel;
        return rel;
    }
};

int main(){
    Solution sol;
    string a = "words and -0";
    cout << sol.myAtoi(a)<<endl;
    cout << sol.myItoa(sol.myAtoi(a))<<endl;
    return 0;
}