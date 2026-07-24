//
// Created by Kotake on 2021/8/3.
//
#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int divide(int dividend, int divisor) {
        assert(divisor != 0);
        int count = 0, result = 0;
        bool isNeg = false;
        if ((dividend < 0 && divisor > 0) || (dividend > 0 && divisor < 0))
            isNeg = true;
        unsigned int tDividend = abs(dividend);
        unsigned int tDivisor = abs(divisor);
        unsigned int sum = 0;
        while (tDivisor < tDividend) {
            count = 1;
            sum = tDivisor;
            while ((sum <<= 1) < tDividend) {
                count <<= 1;
            }
            tDividend -= (sum >>= 1);
            result += count;
        }
        if (tDivisor == tDividend)
            result++;
        return isNeg ? (0 - result) : result;
    }
};

int main() {
    Solution sol;
    int m, n;
    cin >> m >> n;
    cout << sol.divide(m, n);
}