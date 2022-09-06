/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
    
private:
    int parseTree(TreeNode* node){
        
        if(node == nullptr){
            return 0;
        }
        
        int leftResult = parseTree(node->left);
        
        if(leftResult == 0 ){
            node->left = nullptr;
        }
        
        int rightResult = parseTree(node -> right);
        
        if(rightResult == 0 ){
            node->right = nullptr;
        }
        
        if(leftResult == 0 && rightResult == 0 && node->val == 0 ){
            return 0;
        }
        else{
            return 1;
        }
        
    }

public:
    TreeNode* pruneTree(TreeNode* root) {
        
        int result = parseTree(root);
            
        if(result == 0 ){
            return nullptr;
        }
        else{
            return root;
        }
        
        
    }
};