//
// Created by Administrator on 2021/8/2.
//

#include <vector>
#include <iostream>
#include <cstdlib>
#include <time.h>

using namespace std;
#define ll long long

void quick_sort(vector<int> &s, int l, int r) {
    if (l > r) {
        return;
    }
    int ra=0;
    if(l!=r)
        ra = rand()%(l-r);
    swap(nums[l+ra],nums[l]);
    int i, j, t, temp;
    temp = s[l];
    i = l;
    j = r;
    while (i != j) {
        while (s[j] >= temp && i < j)
            j--;
        while (s[i] <= temp && i < j)
            i++;
        if (i < j) {
            t = s[i];
            s[i] = s[j];
            s[j] = t;
        }
    }
    s[l] = s[i];
    s[i] = temp;
    quick_sort(s, l, i - 1);
    quick_sort(s, i + 1, r);
}

void printIntV(const vector<int> s) {
    for (int i : s) {
        cout << i << ' ';
    }
    cout << endl;
}

int main() {
    int n;
    cin >> n;
    vector<int> v;
    srand(time(NULL));
    for (int i = 0; i < n; i++) {
        v.push_back(rand());
    }
    printIntV(v);
    quick_sort(v, 0, n - 1);
    printIntV(v);

    return 0;
}