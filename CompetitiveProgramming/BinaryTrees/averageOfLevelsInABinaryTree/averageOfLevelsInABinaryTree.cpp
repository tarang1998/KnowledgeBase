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
public:
    vector<double> averageOfLevels(TreeNode* root) {
        
        map<int, vector<int>> levelNodes;
        
        vector<double> results;
        
        parseTree(root,0,levelNodes);
        
        for(int i = 0; i < levelNodes.size(); i++){
            
            vector<int> arr = levelNodes[i];
            
            double sum = 0 ;
            for(int j = 0 ; j <arr.size(); j++){
                sum += arr[j];
            }
            
            results.push_back(sum/arr.size());
        }
                    
        return results;
        
    }
    
private:
    void parseTree(TreeNode* node, int level, map<int,vector<int>> &levelNodes ){
        
        if(node == nullptr){
            return;
        }
        
        if(levelNodes.find(level) == levelNodes.end()){
            
            vector<int> levelNode;
            levelNode.push_back(node->val);
            levelNodes.insert(pair<int,vector<int>>(level,levelNode));
        }
        else{
            levelNodes[level].push_back(node->val);
            
        }
        
        parseTree((node->left),level+1,levelNodes);
        parseTree(node->right,level+1,levelNodes);

        
    }
};