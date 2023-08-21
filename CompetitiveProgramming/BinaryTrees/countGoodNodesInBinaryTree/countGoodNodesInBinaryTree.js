/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */


 var goodNodes = function(root) {
    
    result = []
    
    parseTree(root, root.val,result)
    
    return result.length
    
    
};

var parseTree = function(node, maxValue,result){  
    
    if(node == null || node == undefined){
        return
    }
    
    if(maxValue <= node.val){
        
        result.push(node)
        maxValue = node.val
        
    }
    
    
    parseTree(node.left,maxValue,result)
    
    parseTree(node.right,maxValue,result)
    
    
}
    