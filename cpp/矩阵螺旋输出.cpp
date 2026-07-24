//矩阵螺旋输出
#include <iostream>
#include <malloc.h>

using namespace std;

int main() {
    int m, n;
    cin >> m >> n;
    int **num = (int **) malloc(sizeof(int **));
    for (int i = 0; i < m; i++) {
        int *temp = (int *) malloc(sizeof(int) * n);
        num[i] = temp;
    }
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            cin >> num[i][j];
        }
    }

    int flag = 1;
    int row = 0, col = 0;
    int index = 0;
    while (m && n) {
        index = n;
        while (index--) {
            cout << num[row][col] << ' ';
            col += flag;
        }
        col -= flag;
        row += flag;
        m--;
        if (m == 0)break;
        index = m;
        while (index--) {
            cout << num[row][col] << ' ';
            row += flag;
        }
        row -= flag;
        col -= flag;
        n--;
        if (n == 0)break;
        flag *= -1;
    }
    return 0;
}