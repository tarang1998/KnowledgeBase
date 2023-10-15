class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        
        n = len(grid)
        m = len(grid[0])
        
        prefix = [1]
        suffix = [1]

        for i in range(n):
            for j in range(m):
                prefix.append((prefix[-1] * grid[i][j])%12345)
                suffix.append((suffix[-1] * grid[~i][~j])%12345)

       
        for i in range(n):
            for j in range(m):
                k = (i * m)+ j 

                grid[i][j] = (prefix[k] * suffix[(-k-2)]) % 12345

        return grid
            
                
                