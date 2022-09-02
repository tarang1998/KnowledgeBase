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
 * @return {number[]}
 */


 var averageOfLevels = function(root) {
    
    levelNodes = []
    
    parseTree(root,0,levelNodes)
    
    results = []
    
    
    for(let i = 0;i<levelNodes.length;i++){
        results.push(levelNodes[i].reduce((a,b)=> a+b , 0)/levelNodes[i].length)
    }
    
    
    return results
    
};


var parseTree = function(node,level,levelNodes) {
    
    
    if(node == null ){
        return
    }
    

    
    if(levelNodes[level] != null){
        levelNodes[level].push(node.val)
    }
    else{
        levelNodes[level] = [node.val]
    }
    
    parseTree(node.left,level+1,levelNodes)
    parseTree(node.right,level+1,levelNodes)
    

}