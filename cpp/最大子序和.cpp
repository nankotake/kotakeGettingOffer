//
// Created by Kotake on 2021/8/31.
//

#include "bits/stdc++.h"

int main() {
    vector<int> a = {-1,-2,5,-3,-4,1000};
    int pre = 0, maxAns = a[0];
    for (const auto &x: a) {
        pre = max(pre + x, x);
        maxAns = max(maxAns, pre);
    }
    cout << maxAns;
}