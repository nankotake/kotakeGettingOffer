//
// Created by Kotake on 2021/8/7.
//
#include "bits/stdc++.h"

using namespace std;

struct ListNode {
    int val;
    ListNode *next;

    ListNode() : val(0), next(nullptr) {}

    ListNode(int x) : val(x), next(nullptr) {}

    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode *mergeTwoLists(ListNode *l1, ListNode *l2) {
        if (l1 == NULL)return l2; else if (l2 == NULL)return l1;
        ListNode *LH = new ListNode();
        ListNode *LM = LH, *p1 = l1, *p2 = l2;
        while (p1 && p2) {
            if (p1->val <= p2->val) {
                LM->next = p1;
                LM = LM->next;
                p1 = p1->next;
            } else {
                LM->next = p2;
                LM = LM->next;
                p2 = p2->next;
            };
        }
        if (p1 != NULL)LM->next = p1;
        else if (p2 != NULL)LM->next = p2;
        return LH->next;
    }
};

int main() {
    vector<int> a={1,1,2,3},
                b={2,2,3,4};
    ListNode *aa=new ListNode(0,NULL),*bb=new ListNode(0,NULL),*p;
    p=aa;
    for(int i:a){
        ListNode *temp = new ListNode(i,NULL);
        p->next=temp;
        p=p->next;
    }
    p=bb;
    for(int i:b){
        ListNode *temp = new ListNode(i,NULL);
        p->next=temp;
        p=p->next;
    }
    Solution sol;
    ListNode *rel = sol.mergeTwoLists(aa->next,bb->next);
    for(p=rel;p!=NULL;p=p->next){
        cout << p->val << ' ';
    }
    return 0;
}