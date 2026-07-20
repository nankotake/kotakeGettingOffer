//
// Created by Kotake on 2021/7/27.
//

#include <vector>
#include <iostream>
#include <unordered_map>

using namespace std;

class record {
public:
    int time;
    vector<int> pos;

    record() { time = 0; };
};

int main() {
    int n, m;
    cin >> n >> m;
    vector<record> r;
    vector<int> rel;
    for (int i = 0; i < n; i++) {
        record t;
        t.time = 0;
        r.push_back(t);
    }
    for (int i = 0; i < n; i++) {
        int t;
        cin >> t;
        rel.push_back(t);
        r[t].time += 1;
        r[t].pos.push_back(i);
    }
    for (vector<record>::iterator it = r.begin(); it != r.end(); it++) {
        if (it->time > m) {
            for (int i = 0; i < it->pos.size(); i++) {
                rel[it->pos[i]] = -1;
            }
        }
    }
    for (int i = 0; i < n; i++) {
        if (rel[i] != -1)cout << rel[i] << ' ';
    }
}