//
// Created by Kotake on 2021/8/21.
//
/*
 * 小朋友围一圈发纸，如果比旁边的年纪大就要多，求一共最少多少
*/
#include "bits/stdc++.h"

using namespace std;

int atoi(string i) {
    int rel = 0;
    bool flag = true;
    if (i[0] == '-') {
        flag = false;
        i[0] = '0';
    }
    for (char j : i) {
        rel = rel * 10 + j - '0';
    }
    return flag ? rel : (0 - rel);
}

class child {
public:
    int i;
    int age;

    child(int ii, int aa) : i(ii), age(aa) {};
};

bool sorter(child c1, child c2) {
    return c1.age > c2.age;
}

int solution(vector<int> ages) {
    int count = 0;
    int size = ages.size();
    vector<int> paper(size, 0);
    vector<child> children;
    for (int i = 0; i < size; i++) {
        children.push_back(child(i, ages[i]));
    }
    sort(children.begin(), children.end(), sorter);
    for (auto c : children) {
        int index = c.i;
        if (index == 0) {
            if (ages[index] > ages[1] && ages[index] > ages[ages.size() - 1]) {
                paper[index] = max(paper[1], paper[ages.size() - 1]) + 1;
            } else if (ages[index] > ages[1]) {
                paper[index] = paper[1] + 1;
            } else if (ages[index] > paper[ages.size() - 1]) {
                paper[index] = paper[ages.size() - 1] + 1;
            } else {
                paper[index] = 1;
            }
        } else if (index == ages.size() - 1) {
            if (ages[index] > ages[0] && ages[index] > ages[ages.size() - 2]) {
                paper[index] = max(paper[0], paper[ages.size() - 2]) + 1;
            } else if (ages[index] > ages[0]) {
                paper[index] = paper[0] + 1;
            } else if (ages[index] > ages[ages.size() - 2]) {
                paper[index] = paper[ages.size() - 2] + 1;
            } else {
                paper[index] = 1;
            }
        } else {
            if (ages[index] > ages[index - 1] && ages[index] > ages[index + 1]) {
                paper[index] = max(paper[index - 1], paper[index + 1]) + 1;
            } else if (ages[index] > ages[index + 1]) {
                paper[index] = paper[index + 1] + 1;
            } else if (ages[index] > ages[index - 1]) {
                paper[index] = paper[index - 1] + 1;
            } else {
                paper[index] = 1;
            }
        }
    }
    for (int i : paper)
        count += i;
    return count;
}

int main() {
    char temp;
    string t;
    int index = 0;
    vector<int> m;
    while (temp = getchar()) {
        if (temp == ' ') {
            m.push_back(atoi(t));
            t.clear();
        } else if (temp == '\n') {
            if (!t.empty())
                m.push_back(atoi(t));
            break;
        } else {
            t = t + temp;
        }
    }

    cout << solution(m);

    return 0;
}