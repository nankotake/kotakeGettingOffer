//
// Created by Administrator on 2021/8/10.
//
//给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。
//
//请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
#include "bits/stdc++.h"

using namespace std;

class Solution {
public:
    void maxHeapify(vector<int> &a, int i, int heapSize) {
        int l = i * 2 + 1, r = i * 2 + 2, largest = i;
        cout << "l:" << l << " r:" << r << endl;
        if (l < heapSize && a[l] > a[largest]) {
            largest = l;
        }
        if (r < heapSize && a[r] > a[largest]) {
            largest = r;
        }
        if (largest != i) {
            swap(a[i], a[largest]);
            maxHeapify(a, largest, heapSize);
        }
    }

    void buildMaxHeap(vector<int> &a, int heapSize) {
        for (int i = heapSize / 2; i >= 0; --i) {
            // cout << "i:"<<i << endl;
            maxHeapify(a, i, heapSize);
        }
    }

    int findKthLargest(vector<int> &nums, int k) {
        int heapSize = nums.size();
        if (k > heapSize)
            return -1;
        buildMaxHeap(nums, heapSize);
        for (int i = nums.size() - 1; i >= nums.size() - k + 1; --i) {
            swap(nums[0], nums[i]);
            --heapSize;
            maxHeapify(nums, 0, heapSize);
        }
        return nums[0];
    }
};

class Solution2 {
public:
    int quickSelect(vector<int>& a, int l, int r, int index) {
        int q = randomPartition(a, l, r);
        if (q == index) {
            return a[q];
        } else {
            return q < index ? quickSelect(a, q + 1, r, index) : quickSelect(a, l, q - 1, index);
        }
    }

    inline int randomPartition(vector<int>& a, int l, int r) {
        int i = rand() % (r - l + 1) + l;
        swap(a[i], a[r]);
        return partition(a, l, r);
    }

    inline int partition(vector<int>& a, int l, int r) {
        int x = a[r], i = l - 1;
        for (int j = l; j < r; ++j) {
            if (a[j] <= x) {
                swap(a[++i], a[j]);
            }
        }
        swap(a[i + 1], a[r]);
        return i + 1;
    }

    int findKthLargest(vector<int>& nums, int k) {
        srand(time(0));
        return quickSelect(nums, 0, nums.size() - 1, nums.size() - k);
    }
};

int main() {
    vector<int> a = {3, 2, 3, 1, 2, 4, 5,2,1};
    int k = 3;
//    Solution sol;
//    cout << sol.findKthLargest(a, k) << endl;
    Solution2 sol2;
    cout << sol2.findKthLargest(a, k) << endl;
}