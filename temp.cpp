#include <vector>
#include <iostream>

using namespace std;

void qs(vector<int> &a, int l, int r) {
    if (l > r)return;
    int i = l, j = r;
    int stand = a[l];
    while (i != j) {
        while (a[j] >= stand && i < j) { j--; }
        while (a[i] <= stand && i < j) { i++; }
        if (i < j) {
            int temp = a[i];
            a[i] = a[j];
            a[j] = temp;
            j--;
            i++;
        }
    }
    a[l] = a[i];
    a[i] = stand;
    qs(a, l, i - 1);
    qs(a, i + 1, r);
}

int main() {
    int m;
    cin >> m;
    vector<int> a;
    for (int i = 0; i < m; i++) {
        int temp;
        cin >> temp;
        a.push_back(temp);
    }
    qs(a, 0, a.size() - 1);
    for (int i = 0; i < a.size(); i++) {
        cout << a[i] << ' ';
    }
    return 0;
}