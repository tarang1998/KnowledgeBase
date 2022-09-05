/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> children;

    Node() {}

    Node(int _val) {
        val = _val;
    }

    Node(int _val, vector<Node*> _children) {
        val = _val;
        children = _children;
    }
};
*/

class Solution {
    
private:
    void parseTree(Node* node,int level,vector<vector<int>> &results){
        
        
        if(node == nullptr){
            return;
        }
        
        if(results.size() == level){
            vector<int> levelNodes {node->val};
            results.push_back(levelNodes);
        }
        else{
            results[level].push_back(node->val);
        }
        
        for(int i = 0 ;i < node->children.size(); i++){
            parseTree(node->children[i],level+1,results);
        }
        
    }
    
    
public:
    vector<vector<int>> levelOrder(Node* root) {
        
        vector<vector<int>> results;
        
        parseTree(root,0,results);
            
        return results;
        
    }
};