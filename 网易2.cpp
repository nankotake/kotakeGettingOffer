//
// Created by Kotake on 2021/8/21.
//
/*
 * Sn = Sn-1 + Ln + revert(invert(Sn-1))
*/
#include "bits/stdc++.h"
class Solution {
public:
    /**
     * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
     *
     * 返回Sn的第k位字符
     * @param n int整型 Sn的n
     * @param k int整型 需要返回的字符下标位
     * @return char字符型
     */
    string invert(string temp){
        string a = temp;
        for(int i=0;i<a.size();i++){
            a[i] = a[i]+(25-2*(a[i]-'a'));
        }
        return a;
    }
    string revert(string temp){
        string a = temp;
        for(int i=0,j=a.size()-1;i<=j;i++,j--){
            swap(a[i],a[j]);
        }
        return a;
    }
    char findKthBit(int n, int k) {
        // write code here
        string s="a";
        int count=1;
        for(;count<=n;count++){
            s = s + char('a'+count) + revert(invert(s));
        }
        return s[k-1];
    }
};

int main(){
    Solution sol;
    string temp = "abc";
    cout << sol.revert(temp);
    cout << sol.invert(temp);
    cout << sol.findKthBit(3,1);
}