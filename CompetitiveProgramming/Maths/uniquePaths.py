# https://leetcode.com/problems/unique-paths/

class Solution:
    
    pathCount = 0 
    
    isMemoInitialized = False
    
    memo = []
    
    def initializeMemo(self):
        
        
        for i in range(100):
            row = []
            for j in range(100):
                row.append(None) 
            self.memo.append(row)
            
        #Setting the bottom row in memo to 1 
        for i in range(0,100):
            self.memo[99][i] = 1
            
        #Setting the right most column in memo to 1
        for i in range(0,100):
            self.memo[i][99] = 1
            
            
        for c in range(98,-1,-1):
            for r in range(98,-1,-1):

                val = self.memo[r+1][c] + self.memo[r][c+1] 

                self.memo[r][c]  = val


                
                
        self.isMemoInitialized = True 

                
        
    
    
    
    def findPathsBruteForce(self,m,n,r,c):
        
        if(r == m-1 and c == n-1):
            self.pathCount += 1 
            return 
        
        #Moving down 
        if(r != m-1):
            self.findPaths(m,n,r+1,c)
            
        #Moving right 
        if(c != n-1):
            self.findPaths(m,n,r,c+1)
            
    def solve(self,m,n,r,c,dp):
        
        
        if(r < 0 ):
            return 0 
        
        if(c > n-1):
            return 0 
        
        if((r == 0 ) or (c == 0 )):
            return 1
        
        dp[r][c] = self.solve(m,n,r,c-1,dp) + self.solve(m,n,r-1,c,dp)
        return dp[r][c]
            
    
    
    def uniquePaths(self, m: int, n: int) -> int:
        
        #dp = [[0]*n for _ in range(m)]
        
        #val = self.solve(m,n,m-1,n-1,dp)
                
        #return val
        
        
        
        if(not self.isMemoInitialized):
            self.initializeMemo()
        return self.memo[99-m+1][99-n+1]       
        
        
        #self.findPathsBruteForce(m,n,0,0)
        
        #return self.pathCount
        
        
        