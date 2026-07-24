//有序数组合并
#include <iostream>

using namespace std;

int main() {
    int a[5] = {1, 2, 3, 0, 0};
    int b[2] = {4, 5};
    int i = 2, j = 1, id = 4;
    for (; i >= 0 && j >= 0;) {
        if (a[i] > b[j]) { a[id--] = a[i--]; }
        else { a[id--] = b[j--]; }
    }
    while (j >= 0)
        a[index--] = b[j--];
    cout << a[0] << a[1] << a[2] << a[3] << a[4];
}