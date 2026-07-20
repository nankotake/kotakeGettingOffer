//
// Created by Kotake on 2021/8/21.
//
#include "bits/stdc++.h"

struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};


class Solution {
private:
    vector<vector<int>> paths;
    vector<int> path;
public:
    /**
     *
     * @param root TreeNode类
     * @param sum int整型
     * @return int整型vector<vector<>>
     */
    void dfs(TreeNode *root, int sum, vector<int> list, vector<vector<int>> result) {
        cout << "?";
        if(root==NULL)return;
        list.push_back(root->val);
        if(root->left==NULL && root->right==NULL){
            if(sum==root->val)result.push_back(list);
        }
        list.pop_back();
        dfs(root->left,sum-root->val,list,result);
        dfs(root->right,sum-root->val,list,result);
        list.pop_back();
    }

    vector<vector<int>> pathSum(TreeNode *root, int sum) {
        vector<vector<int>> result;
        dfs(root, sum, vector<int>(), result);
        return result;
    }
};
int main(){
    Solution sol;
    vector<int> a = {1,2,3};
    for(int i : a){

    }
    TreeNode *root = new TreeNode;
    root->val=1;
    root->right=NULL;
    root->left=NULL;
    vector<vector<int>> result = sol.pathSum(root,1);
    cout << endl;
    return 0;
}