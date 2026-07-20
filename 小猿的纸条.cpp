//
// Created by Kotake on 2021/7/31.
// 小猿有两张分别写着字符串s1、s2的纸条，字符串由大小写字母组成。小猿会进行n次操作，
// 每次操作时小猿会选择其中一张纸条，把它从左侧撕下一段或把它全部交给你。
// 你按收到纸条的顺序，从左到右将收到的n张纸条拼接成一张新的纸条。
// 已知字符串s1、s2，求是否存在一种方案使新纸条上的字符串与s3相同、且满足n<=K。
//
#include <iostream>
#include <string>

using namespace std;

string a, b, c;

bool countNum(int indexc, int indexa, int indexb, int k, int flag) {
    if (k < 0) {
        return false;
    }
    if (indexc == c.size()) {
        return true;
    }
    if (indexa < a.size() && a[indexa] == c[indexc]) {

        if (countNum(indexc + 1, indexa + 1, indexb, (flag == 0) ? k : k - 1, 0)) {
            return true;
        }
    }
    if (indexb < b.size() && b[indexb] == c[indexc]) {
        if (countNum(indexc + 1, indexa, indexb + 1, (flag == 1) ? k : k - 1, 1)) {
            return true;
        }
    }
    return false;

}

int main() {
    int t;
    cin >> t;
    int k;
    while (t--) {
        cin >> a >> b >> c;
        cin >> k;
        if (countNum(0, 0, 0, k, -1)) {
            cout << 1 << endl;
        } else {
            cout << 0 << endl;
        }
    }
    return 0;
}