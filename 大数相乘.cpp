#include <string>
#include <iostream>
#include <stack>

using namespace std;

string pow(string a, int p) {
    if (a == "0")return a;
    for (int i = 0; i < p; i++)
        a += '0';
    return a;
}

string bigIntAdd(string a, string b) {
    int alen = a.size();
    int blen = b.size();
    int maxLen = alen > blen ? alen : blen;
    int minLen = alen < blen ? alen : blen;
    string max = alen > blen ? a : b;
    string min = alen < blen ? a : b;
    if (maxLen == minLen) {
        max = a;
        min = b;
    }
    for (int i = minLen - 1, j = maxLen - 1; i >= 0; i--, j--) {
        max[j] += min[i] - '0';
        if (max[j] > '9') {
            if (j > 0) {
                max[j - 1]++;
                max[j] -= 10;
            } else {
                max = "1" + max;
                max[j] -= 10;
            }
        }
    }
    if (max[0] > '9') {
        max = "1" + max;
        max[1] -= 10;
    }
    return max;
}

string bigIntMul(string a, string b) {
    if (a[0] == 0 || b[0] == 0)return "0";
    bool minus = false;
    if (a[0] == '-' || b[0] == '-') {
        if (a[0] == '-' && b[0] == '-')minus = false;
        else minus = true;
    }
    if (a[0] == '-')a.erase(a.begin());
    if (b[0] == '-')b.erase(b.begin());
    int aa, bb;
    char c1 = '0', c2 = '0';
    string rel[a.size()];
    for (int i = a.size() - 1; i >= 0; i--) {
        aa = a[i] - '0';
        if (aa == 0) {
            rel[a.size() - 1 - i] = "0";
            continue;
        }
        for (int j = b.size() - 1; j >= 0; j--) {
            bb = b[j] - '0';
            c1 = ((aa * bb) + c2 - '0') % 10 + '0';
            c2 = ((aa * bb) + c2 - '0') / 10 + '0';
            rel[a.size() - 1 - i] = c1 + rel[a.size() - 1 - i];
        }
        if (c2 != '0')
            rel[a.size() - 1 - i] = c2 + rel[a.size() - 1 - i];
        c2 = '0';
        c1 = '0';
    }
    for (int i = 0; i < a.size(); i++) {
        rel[i] = pow(rel[i], i);
    }

    string sum = "0";
    for (int i = 0; i < a.size(); i++) {
        sum = bigIntAdd(sum, rel[i]);
    }
    if (minus)sum = "-" + sum;
    return sum;
}


int main() {
    string a, b;
    a = "9";
    b = "999999999999999999999994";
    //    cin >> a >> b;
    //    cout << bigIntAdd(a,b);
    cout << bigIntMul(a, b);
}