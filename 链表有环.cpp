//
// Created by Kotake on 2021/8/22.
//

#include "bits/stdc++.h"
class Solution {
public:
    bool hasCycle(ListNode *head) {
        if(head==NULL || head->next==NULL)return false;
        ListNode *p1=head,*p2=head;
        while(p1 && p2){
            p1=p1->next;
            p2=p2->next;
            if(p2)
                p2=p2->next;
            if(p1==p2)return true;
        }
        return false;
    }
};
int main(){

}