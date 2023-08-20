/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */


class Solution {
    
    public TreeNode lowestCommonAncestor;
    
    public TreeNode parseTree(TreeNode node, TreeNode p, TreeNode q){
        
        if(node == null){
            return null;
        }
        
        if(p.val == node.val){
            return node;
        }
        
        if(q.val == node.val){
            return node;
        }
        
        if((p.val < node.val  && q.val > node.val) || (p.val > node.val  && q.val < node.val)){
            return node;
        }
        
        if(p.val < node.val && q.val < node.val){    
            return parseTree(node.left,p,q);         
        }
        
        if(p.val > node.val && q.val > node.val){      
           return parseTree(node.right,p,q);          
        }
        
        return null;
          
    }
    
    
    
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        
        return parseTree(root,p,q); 
                     
    }
    
}