//
// Created by Kotake on 2021/8/30.
//

#include "bits/stdc++.h"
class Solution {
public:
    // 翻转一个子链表，并且返回新的头与尾
    pair<ListNode*, ListNode*> myReverse(ListNode* head, ListNode* tail) {
        ListNode* prev = tail->next;
        ListNode* p = head;
        while (prev != tail) {
            ListNode* nex = p->next;
            p->next = prev;
            prev = p;
            p = nex;
        }
        return {tail, head};
    }

    ListNode* reverseKGroup(ListNode* head, int k) {
        ListNode* hair = new ListNode(0);
        hair->next = head;
        ListNode* pre = hair;

        while (head) {
            ListNode* tail = pre;
            // 查看剩余部分长度是否大于等于 k
            for (int i = 0; i < k; ++i) {
                tail = tail->next;
                if (!tail) {
                    return hair->next;
                }
            }
            ListNode* nex = tail->next;
            pair<ListNode*, ListNode*> result = myReverse(head, tail);
            head = result.first;
            tail = result.second;
            // 把子链表重新接回原链表
            pre->next = head;
            tail->next = nex;
            pre = tail;
            head = tail->next;
        }
        return hair->next;
    }
};
int main(){
    vector<int> a={1,2,3,4,5,6,7,8,9,10,11,12};
    int k=5;
    Solution sol;
    ListNode *pre=nullptr;
    for(int i=a.size()-1;i>=0;i--){
        auto temp=new ListNode(a[i],pre);
        pre = temp;
    }
    ListNode *rel = sol.reverseKGroup(pre,k);
    for(auto p=rel;p!=nullptr;p=p->next){
        cout << p->val << ' ';
    }
    cout << endl;
    return 0;
}