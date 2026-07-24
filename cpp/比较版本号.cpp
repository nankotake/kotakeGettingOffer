//
// Created by Kotake on 2021/9/1.
//

#include "bits/stdc++.h"

int atoi(string i) {
    if (i == "")return 0;
    int rel = 0;
    bool flag = true;
    if (i[0] == '-') {
        flag = false;
        i[0] = '0';
    }
    for (char j : i) {
        rel = rel * 10 + j - '0';
    }
    return flag ? rel : (0 - rel);
};

class Solution {
public:
    /**
     * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
     *
     * 比较版本号
     * @param version1 string字符串
     * @param version2 string字符串
     * @return int整型
     */
    vector<string> get(string v) {
        vector<string> a, aa, aaa;
        string temp;
        for (char i : v) {
            if (i == '.') {
                a.emplace_back(temp);
                temp = "";
            } else temp += i;
        }
        a.emplace_back(temp);
        temp = "";
        for (auto i : a) {
            bool flag = true;
            for (char j : i) {
                if (j != '0') {
                    flag = false;
                }
                if (j != '0' || !flag) {
                    temp += j;
                }
            }
            if (flag == true)
                temp = i;
            aa.emplace_back(temp);
            temp = "";
        }
//        for(int i=0;i<aa.size();i++){
//            bool flag=true;
//            for(int j=aa[i].size()-1;j>=0;j--){
//                if(aa[i][j]!='0'){
//                    flag=false;
//                    temp.insert(temp.begin(),aa[i][j]);
//                }
//                else if(aa[i][j]!='0' && !flag)temp.insert(temp.begin(),aa[i][j]);
//            }
//            if(flag==true)
//                temp=aa[i];
//            aaa.emplace_back(temp);
//            temp="";
//        }
        return aa;
    }

    int compareVersion(string version1, string version2) {
        // write code here
        vector<string> aa = get(version1), bb = get(version2);
        bool flag = true;
        for (int i = aa.size() - 1; i >= 0; i--) {
            if (atoi(aa[i]) == 0) {
                aa.pop_back();
            } else if (atoi(aa[i]) != 0)break;
        }
        for (int i = bb.size() - 1; i >= 0; i--) {
            if (atoi(bb[i]) == 0) {
                bb.pop_back();
            } else if (atoi(bb[i]) != 0)break;
        }
        string temp;
        int i = 0;
        for (; i < aa.size() && i < bb.size(); i++) {
            int a = atoi(aa[i]), b = atoi(bb[i]);
            if (a > b)return 1;
            else if (a < b)return -1;
        }
        if (i < bb.size())return -1;
        else if (i < aa.size())return 1;
        return 0;
    }
};

int main() {
    string a = "1.0.0", b = "1.0";
    Solution sol;
    cout << sol.compareVersion(a, b);
    return 0;
}