//开根号
#include <iostream>

using namespace std;

float sqrt(float n) {
    float max, min, mid;
    max = n;
    min = 0;
    mid = max / 2;
    while (1) {
        if (n - mid * mid < 0.001 && mid * mid - n < 0.01)break;
        mid = (min + max) / 2;
        if (mid * mid > n) {
            max = mid;
        } else if (mid * mid == n)return mid;
        else { min = mid; }
    }
    return mid;
}

int main() {
    cout << sqrt(2) << endl;
    cout << sqrt(3) << endl;
    cout << sqrt(4) << endl;
}