class Solution:
    # Time Complexity : O(n*m)
    # Space Complexity : O(n*m)
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

    
        ROWS = len(heights)
        COLS = len(heights[0])

        directions = [(-1,0),(1,0),(0,1),(0,-1)]

        atlantic = {}
        pacific = {}

        def bfs(ocean):

            q = deque()
            q.extend(ocean.keys())

            while q:
                r,c = q.popleft()

                for dr,dc in directions:
                    nr,nc = r+dr, c+dc
                    if nr<0 or nr>=ROWS or nc<0 or nc>=COLS or (nr,nc) in ocean or heights[nr][nc]<heights[r][c]:
                        continue
                    q.append((nr,nc))
                    ocean[(nr,nc)] = 1 

    
        def dfs(r,c,ocean):
            if (r,c) in ocean:
                return 
            
            #Marking the cordinates that can reach the ocean
            ocean[(r,c)] = 1

            for dr,dc in directions:
                nr,nc = r+dr, c+dc
                if nr<0 or nr>=ROWS or nc<0 or nc>=COLS or heights[nr][nc]<heights[r][c]:
                    continue
                dfs(nr,nc,ocean)

        # # Starting dfs from the cells in the left and right borders
        # for r in range(ROWS):
        #     dfs(r,0,pacific)
        #     dfs(r,COLS -1, atlantic)


        # # Starting dfs from the cells in the top and bottom borders
        # for c in range(COLS):
        #     dfs(0,c,pacific)
        #     dfs(ROWS-1,c,atlantic)
           

        # Using bfs
        # Collecting all the cordinates from which 
        # water can flow into the pacific or atlantic ocean 
        for r in range(ROWS):
            pacific[(r,0)]=1
            atlantic[(r,COLS-1)]=1

        for c in range(COLS):
            pacific[(0,c)]=1
            atlantic[(ROWS-1,c)]=1

        bfs(pacific)
        bfs(atlantic)

        result = []

        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pacific and (r,c) in atlantic:
                    result.append([r,c])

        return result
           
                


        