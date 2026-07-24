#include <iostream>

using namespace std;

class NODE {
public:
    int i;
    NODE *next;

    NODE(int ii) {
        i = ii;
        next = NULL;
    };

    NODE() { next = NULL; };

    void printAll(NODE *n) {
        while (n != NULL) {
            cout << n->i << ' ';
            n = n->next;
        }
        cout << endl;
    };
};

int main() {
    NODE *head = new NODE(1);
    NODE *p1, *p2, *p3;
    p1 = head;
    for (int i = 2; i <= 10; i++) {
        NODE *temp = new NODE(i);
        p1->next = temp;
        p1 = temp;
    }
    head->printAll(head);

    p1 = head;
    if (p1->next != NULL) { p2 = p1->next; }
    else {
        head->printAll(head);
        return 0;
    }
    if (p2->next != NULL) { p3 = p2->next; }
    else {
        p2->next = p1;
        p1->next = NULL;
        head = p2;
        head->printAll(head);
        return 0;
    }
    while (p2 != NULL) {
        p2->next = p1;
        p1 = p2;
        p2 = p3;
        if (p3 != NULL) { p3 = p3->next; }
    }
    head->next = NULL;
    head = p1;
    head->printAll(head);
    return 0;
}
