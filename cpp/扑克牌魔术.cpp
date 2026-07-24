//
// Created by Kotake on 2021/7/31.
//
#include <iostream>
#include <vector>

using namespace std;

vector<int> dish(vector<int> a) {
    vector<int> rel;
    int i = 0;
    int j = a.size() / 2;
    int mid = j;
    while (i < mid || j < a.size()) {
        if (j < a.size()) {
            rel.push_back(a[j++]);
        }
        if (i < mid) {
            rel.push_back(a[i++]);
        }
    }
    return rel;
}

int main() {
    int m, n;
    cin >> n >> m;
    vector<int> a;
    for (int i = 0; i < n; i++) {
        int j;
        cin >> j;
        a.push_back(j);
    }
    for (int i = 0; i < m; i++) {
        a = dish(a);
    }
    for (int i = 0; i < n; i++)cout << a[i] << ' ';
}
