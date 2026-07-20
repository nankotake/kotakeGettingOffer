//
// Created by Kotake on 2021/8/20.
//
#include "bits/stdc++.h"

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        int addon=0;
        ListNode *p1=l1,*p2=l2,*pp1,*pp2;;
        if(p1==NULL)return l2;
        if(p2==NULL)return l1;
        while(p1!=NULL && p2!=NULL){
            p2->val=p1->val+p2->val+addon;
            if(p2->val>=10){
                addon=1;
                p2->val-=10;
            }
            else{
                addon=0;
            }
            pp1=p1;pp2=p2;p1=p1->next;p2=p2->next;
        }
        if(p1==NULL && p2!=NULL){
            if(addon==0){
                return l2;
            }
            else{
                while(addon!=0&&p2!=NULL){
                    p2->val+=addon;
                    if(p2->val>=10){
                        addon=1;
                        p2->val-=10;
                    }
                    pp2=p2;p2=p2->next;
                }
                if(p2==NULL && addon == 1){
                    ListNode *end=(ListNode*)malloc(sizeof(ListNode));
                    end->val=1;
                    end->next=NULL;
                    pp2->next=end;
                }
                return l2;
            }
        }
        else if(p2==NULL && p1!=NULL){
            if(addon==0){
                pp2->next=p1;
                return l2;
            }
            else{
                pp2->next=p1;
                while(addon!=0&&p1!=NULL){
                    p1->val+=addon;
                    if(p1->val>=10){
                        addon=1;
                        p1->val-=10;
                    }
                    pp1=p1;p1=p1->next;
                }
                if(p1==NULL && addon == 1){
                    ListNode *end=(ListNode*)malloc(sizeof(ListNode));
                    end->val=1;
                    end->next=NULL;
                    pp1->next=end;
                }
                return l2;
            }
        }
        else if(p2==NULL && p1==NULL && addon==1){
            ListNode *end;end->val=1;end->next=NULL;pp2->next=end;
        }
        return l2;
    }
};

int main(){
    Solution sol;
    ListNode *a = new ListNode(0,NULL),*b=new ListNode(0,NULL),*ap=a,*bp=b;
    vector<int> aa = {1,8},bb={0};
    for(int i : aa){
        ListNode *temp=new ListNode(i,NULL);
        ap->next=temp;
        ap=temp;
    }
    for(int i : bb){
        ListNode *temp=new ListNode(i,NULL);
        bp->next=temp;
        bp=temp;
    }
    cout << sol.addTwoNumbers(a->next,b->next);
    return 0;
}