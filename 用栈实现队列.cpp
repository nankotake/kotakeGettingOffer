//
// Created by Kotake on 2021/8/22.
//
#include "bits/stdc++.h"
class MyQueue {
private:
    stack<int> inStack, outStack;

    void in2out() {
        while (!inStack.empty()) {
            outStack.push(inStack.top());
            inStack.pop();
        }
    }

public:
    MyQueue() {}

    void push(int x) {
        inStack.push(x);
    }

    int pop() {
        if (outStack.empty()) {
            in2out();
        }
        int x = outStack.top();
        outStack.pop();
        return x;
    }

    int peek() {
        if (outStack.empty()) {
            in2out();
        }
        return outStack.top();
    }

    bool empty() {
        return inStack.empty() && outStack.empty();
    }
};

int main(){
    MyQueue *myQueue=new MyQueue();
    myQueue->push(1);
    myQueue->push(2);
    myQueue->push(3);
    myQueue->push(4);
    cout << myQueue->pop() << endl;
    myQueue->push(5);
    cout << myQueue->pop() << endl;
    cout << myQueue->pop() << endl;
    cout << myQueue->pop() << endl;
    cout << myQueue->pop() << endl;
    return 0;
}