//
// Created by Kotake on 2021/8/15.
//
#include <iostream>
#include <stack>
#include <string>
using namespace std;
bool match(string s){
    stack<char> ss;
    for(char & i : s){
        if(i=='('||i=='['||i=='{'){ss.push(i);}
        else if(i==')'){
            if(!ss.empty()&&ss.top()=='('){
                ss.pop();
            }
            else return false;
        }
        else if(i==']'){
            if(!ss.empty()&&ss.top()=='['){
                ss.pop();
            }
            else return false;
        }
        else if(i=='}'){
            if(!ss.empty()&&ss.top()=='{'){
                ss.pop();
            }
            else return false;
        }
    }
    if(!ss.empty())return false;
    return true;
}
int main(){
    string s="（[()]） [][]() ()[()]";
    string ss="（[()] ][]() (][()]";
    cout << match(s)<<endl;
    cout << match(ss)<<endl;
    return 0;
}