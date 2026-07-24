//
// Created by Kotake on 2021/7/31.
//
/*
小猿想对一种前缀表达式求值，该表达式定义如下：
1、每个表达式的形式都是 ( operator arg1 arg2 )，即由左括号，运算符，运算数1，运算数2，右括号组成。

2、运算符包括三种，分别是'+', '-', '*'。

3、运算符一定接收两个运算数，运算数间必须通过空格分隔，运算数可以是另外一个表达式或者不带符号的非负整数（小于10000000）。

(- 0 1) 代表 0 - 1；
(+ 1 2) 代表 1 + 2；
(+ (* 2 3) 1) 也是一个合法的表达式，代表了 2 * 3 + 1
4、在不产生歧义的情况下，空格也可以省略或者冗余。例如，

(+ 0 1) 和 ( +0 1) ，( +   0 1   ) 都被认为是合法的输入，且有相同的意义，代表 0 + 1。
 */

#include <stack>
#include <iostream>
#include <string>
#include <vector>

#define ll long long
ll Mod = 10000000;
using namespace std;

ll opt(char op, ll n1, ll n2) {
    if (op == '*')return n1 * n2;
    else if (op == '/')return n1 / n2;
    else if (op == '+')return n1 + n2;
    else if (op == '-')return n1 - n2;
}

int main() {
    int N;
    cin >> N;
    getchar();
    for (int i = 0; i < N; i++) {
        string a;
        getline(cin, a);
        stack<int> nums;
        stack<char> ops;
        int kh = 0;
        bool flag = false;
        for (int index = 0; index < a.size(); index++) {
            char aa = a[index];
            if (aa == ' ') {}
            else if (aa == '(')kh++;
            else if (aa == ')') {
                if (kh <= 0) {
                    flag = true;
                    break;
                }
                else {
                    if (ops.size() < 1 || nums.size() < 2) {
                        flag = true;
                        break;
                    }
                    ll n1 = nums.top();
                    nums.pop();
                    ll n2 = nums.top();
                    nums.pop();
                    char op = ops.top();
                    ops.pop();
                    nums.push(opt(op, n2, n1) % Mod);
                    kh--;
                }
            } else if (aa <= '9' && aa >= '0') {
                ll temp = aa - '0';
                char aaa = a[index + 1];
                while (aaa <= '9' && aaa >= '0') {
                    temp = temp * 10 + aaa - '0';
                    aaa = a[++index + 1];
                }
                nums.push(temp % Mod);
            } else {
                ops.push(aa);
            }
        }
        if (nums.size() != 1 || ops.size() != 0 || kh > 0 || flag)cout << "invalid" << endl;
        else cout << (nums.top() % Mod + Mod) % Mod << endl;
    }
    return 0;
}