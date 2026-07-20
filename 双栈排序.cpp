// [2,1,3,4] -> [1,2,3,4]
#include <iostream>
#include <stack>
using namespace std;
class Solution
{
public:
    int pp(stack<int> &stk){
        int t=stk.top();stk.pop();return t;
    }
    stack<int> solution1(stack<int> stk)
    {
        stack<int> tmp;
        while (!stk.empty())
        {
            int v = pp(stk);
            if(!tmp.empty() && tmp.top()<=v){
                tmp.push(v);
            }
            else {
                while(!tmp.empty() && tmp.top()>v){
                    stk.push(pp(tmp));
                }
                tmp.push(v);
            }
        }
        return tmp;
    };
    stack<int> solution2(stack<int> stk)
    {
        stack<int> tmp;
        while (!stk.empty())
        {
            int v = pp(stk);
            if(!tmp.empty() && tmp.top()>=v){
                tmp.push(v);
            }
            else {
                while(!tmp.empty() && tmp.top()<v){
                    stk.push(pp(tmp));
                }
                tmp.push(v);
            }
        }
        return tmp;
    };
    void output(stack<int> input)
    {
        for (int i = 0; !input.empty(); i++)
        {
            cout << input.top() << ' ';
            input.pop();
        }
        cout << endl;
    }
};
int main()
{
    Solution solution;
    int m;
    cin >> m;
    stack<int> s;
    for (int i = 0; i < m; i++)
    {
        int temp;
        cin >> temp;
        s.push(temp);
    }
    solution.output(solution.solution1(s));
    solution.output(solution.solution2(s));
    return 0;
}