//
// Created by Kotake on 2021/8/20.
//

#ifndef KOTAKEGETTINGOFFER_STDC_H
#define KOTAKEGETTINGOFFER_STDC_H

#include <iostream>
#include <vector>
#include <unordered_map>
#include <string>
#include <deque>
#include <stack>
#include <list>
#include <limits>
#include <algorithm>
#include <cstdlib>
#include <functional>
#include <numeric>
#include <queue>
#include <regex>
#include <sstream>
#include <unordered_set>
using namespace std;
class ListNode {
public:
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {};
    ListNode(int x) : val(x), next(nullptr) {};
    ListNode(int x, ListNode *next) : val(x), next(next) {};
};
class TreeNode {
public:
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x):val(x),left(NULL),right(NULL){}
};

#endif //KOTAKEGETTINGOFFER_STDC_H
