//
// Created by Administrator on 2021/8/4.
//
#include <vector>
#include <iostream>
#include <queue>
#include <memory.h>

using namespace std;

class Solution {
    int cnt;         // 好橘子数
    int dis[10][10]; //保存最少次数
    int dir_x[4] = {0, 1, 0, -1};
    int dir_y[4] = {1, 0, -1, 0};

public:
    int orangesRotting(vector<vector<int>> &grid) {
        queue<pair<int, int>> Q;      //bfs队列
        memset(dis, -1, sizeof(dis)); // 初始化
        cnt = 0;
        int n = (int) grid.size(), m = (int) grid[0].size(), ans = 0;
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < m; ++j) {
                if (grid[i][j] == 2) {
                    Q.push(make_pair(i, j)); // 加入队列
                    dis[i][j] = 0;           // 坏橘子处dis为0
                } else if (grid[i][j] == 1)
                    cnt += 1; //好橘子++
            }
        }
        while (!Q.empty()) {
            pair<int, int> x = Q.front();
            Q.pop(); // 取出
            for (int i = 0; i < 4; ++i) { // 四个方向
                int tx = x.first + dir_x[i];
                int ty = x.second + dir_y[i];
                if (tx < 0 || tx >= n || ty < 0 || ty >= m || ~dis[tx][ty] || !grid[tx][ty])
                    continue;
                // 边界外/原本就是坏橘子/没有橘子
                dis[tx][ty] = dis[x.first][x.second] + 1; // 按原来的+1
                Q.push(make_pair(tx, ty));                // 加入队列bfs
                if (grid[tx][ty] == 1) {
                    cnt -= 1;
                    ans = dis[tx][ty];
                    if (!cnt)
                        break;
                }
            }
        }
        return cnt ? -1 : ans;
    }
};

int main() {
    Solution sol;
    int m, n, nn;
    cin >> m >> n;
    nn = n;
    vector<vector<int>> a;
    while (m > 0) {
        vector<int> t;
        nn = n;
        while (nn > 0) {
            int temp;
            cin >> temp;
            t.push_back(temp);
            nn--;
        }
        m--;
        a.push_back(t);
    }
    cout << sol.orangesRotting(a);
    return 0;
}