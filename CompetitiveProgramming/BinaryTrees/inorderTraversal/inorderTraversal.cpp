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
    void parseTree(TreeNode* node,vector<int> &result){
        
        if(node == nullptr){
            return;
        }
        
        parseTree(node->left,result);
        
        result.push_back(node->val);
        
        parseTree(node->right,result);
        
        
    }
    
    
public:
    vector<int> inorderTraversal(TreeNode* root) {
        
        vector<int> result;
        
        parseTree(root,result);
        
        return result;
            
            
        
    }


    // Iteractive Approach
    vector<int> inorderTraversal(TreeNode* root){

        vector<int> ans;
        stack<TreeNode*> s;
        TreeNode *curr = root;

        while(true){
            if(curr != NULL){
                s.push(curr);
                curr = curr->left;
            }
            else if(s.empty())
                break;
            else{
                ans.push_back(s.top()->val);
                curr = s.top() -> right;
                s.pop();
            }
        }

        return ans;

    };
    
    
};