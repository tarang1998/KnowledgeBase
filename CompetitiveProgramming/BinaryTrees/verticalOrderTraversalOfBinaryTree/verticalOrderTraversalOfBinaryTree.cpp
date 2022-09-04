
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNaode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

#include<vector> 

class Solution {
    
private:
    int minHorizontalDistance;
    
private:
    int maxHorizontalDistance;


private:
    void parseTree(TreeNode* node, 
                   int level, 
                   int horizontalDistance, 
                   map<int,vector<vector<int>>> &levelNodes) {
        
        
        if(node == nullptr){
            return;
        }
        

        
        if(horizontalDistance > maxHorizontalDistance){
            maxHorizontalDistance = horizontalDistance;
        }
        
        if(horizontalDistance < minHorizontalDistance){
            minHorizontalDistance = horizontalDistance;
        }
        
        vector<int> nodeVector {level,node->val};
        
        if(levelNodes.find(horizontalDistance) == levelNodes.end()){
            
            levelNodes[horizontalDistance].push_back(nodeVector);
        }
        else{
            vector<vector<int>> arr = levelNodes[horizontalDistance];
            
            for(int i = 0; i< arr.size(); i++){
                
                if(level == arr[i][0]){
                    if(node->val <= arr[i][1]){
                        levelNodes[horizontalDistance].insert(levelNodes[horizontalDistance].begin()+i ,nodeVector);
                        break;
                    }
                  
                }
                
                if(level < arr[i][0]){
                    
                    levelNodes[horizontalDistance].insert(levelNodes[horizontalDistance].begin()+i , nodeVector);
                    break;
                        
                }
                
                if(i == arr.size()-1){
                    levelNodes[horizontalDistance].push_back(nodeVector);
                }
                    
                
            }
        }
        
        
        
        parseTree(node->left, level + 1, horizontalDistance -1 , levelNodes);
        parseTree(node->right, level +1 , horizontalDistance +1 ,levelNodes);
        
        return;
        
    }
    
    
public:
    vector<vector<int>> verticalTraversal(TreeNode* root) {
        
        minHorizontalDistance = 0;
        maxHorizontalDistance = 0;
        
        map<int,vector<vector<int>>> levelNodes;
        
        parseTree(root, 0, 0 , levelNodes);
            
        vector<vector<int>> results;
        
        for(int i = minHorizontalDistance ; i <= maxHorizontalDistance ; i++){
            
            vector<vector<int>> arr = levelNodes[i];
                
            vector<int> result;
                
            for(int j = 0 ;j < arr.size(); j++){
                
                result.push_back(arr[j][1]);
                

            }
            
            results.push_back(result);
        }

        
        return results;
        
        
    }
};