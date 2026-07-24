#include <iostream>
#include <vector>

using namespace std;

void sort(vector<int> &n, int step, int start) {
    for (int i = start + step; i < n.size(); i += step) {
        int k = n[i];
        int j = i - step;
        while (j >= 0 && n[j] > k) {
            n[j + step] = n[j];
            j -= step;
        }
        n[j + step] = k;
    }
}

int main() {
    vector<int> n = {12, 11, 8, 9, 1, 13, 4, 16, 7, 14, 3, 10, 5, 2, 15, 6};
    int step = 4;
    for (step = 4; step >= 1; step--) {
        for (int j = 0; j < step; j++) {
            sort(n, step, j);
        }
    }
    cout << endl;
    for (int i : n)
        cout << i << ' ';
    cout << endl;
}