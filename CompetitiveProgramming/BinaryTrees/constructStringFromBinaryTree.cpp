
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
    string parseTree(TreeNode* node){
        
        string result;
        
        if(node == nullptr){
            return result;
        }
        
        result += to_string(node->val);
        
        string leftVal = parseTree(node->left);
        
        string rightVal = parseTree(node->right);
        
        if(leftVal.empty() and rightVal.empty()){
            return result;
        }
        
        if(!leftVal.empty()){
            result = result + '(' + leftVal + ')';
        }
        else{
            result = result + '(' + ')';
        }
        
        if(!rightVal.empty()){
            result = result + '(' + rightVal + ')';
        }
        
        return result;
            
    }

public:
    string tree2str(TreeNode* root) {
    
        return parseTree(root);
                
        
        
    }
};