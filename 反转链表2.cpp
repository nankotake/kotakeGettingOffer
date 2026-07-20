#include <iostream>
#include <vector>
using namespace std;
struct ListNode
{
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution
{
public:
    ListNode *reverseBetween(ListNode *head, int left, int right)
    {
        ListNode *dump=new ListNode(-1,head);
        if(left>=right)return head;
        ListNode *p=dump,*m,*n;
        for(int i=0;i<left;i++){
            p=p->next;
        }
        m=p->next;
        n=p->next->next;
        for(int i=0;i<right-left && ;i++){
            ListNode *temp=n->next;
            n->next=m;
            m=n;
            n=temp;
        }
        p->next->next=n;
        p->next=m;
        return dump->next;
    }
};

int main()
{
    Solution sol;
    vector<int> temp = {1, 2, 3, 4, 5};
    ListNode *head, *p;
    head->val = -1;
    p = head;
    for (int i : temp)
    {
        ListNode *t;
        t->val = i;
        p->next = t;
        p = t;
        p->next = NULL;
    }
    head = sol.reverseBetween(head->next, 2, 4);
    for (p = head; p != NULL; p = p->next)
    {
        cout << p->val << ' ';
    }
    return 0;
}