from collections import deque, defaultdict 

class Solution:
    
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        
        if endWord not in wordList:
            return []
        
        d = defaultdict(list)
        visited = {}
        
        wordList.append(beginWord)
        
        for word in wordList:
            visited[word] = 0
            for i in range(len(word)):
                d[word[:i]+"*"+word[i+1:]].append(word)
                
        
        ans = []
        
        # Creating a graph from the endWord
        graph = defaultdict(list)
        
        bfsqueue = [endWord]
        visited[endWord] = 1
        
        while(len(bfsqueue) != 0):
            
            ele = bfsqueue.pop(0)
            
            if(ele == beginWord):
                break
            
            for i in range(len(ele)):
                
                nextElePattern = ele[:i] + '*' + ele[i+1:]
                
                nextWords = d[nextElePattern]
                
                for nextWord in nextWords:
                    if(visited[nextWord] == 0):
                        visited[nextWord] = 1
                        graph[ele].append(nextWord)
                        graph[nextWord].append(ele)
                        bfsqueue.append(nextWord)
                            
        #Backtracking from the beginning Word
    
        dfsvisited = {}
        
        
        def dfs(nodeWord,result):
            
            if(nodeWord == endWord):
                ans.append(result)
                return
            
            if(nodeWord not in dfsvisited ):
                for i in range(len(nodeWord)):

                    nextWordPattern = nodeWord[:i]+"*"+nodeWord[i+1:]

                    nextWords = d[nextWordPattern]

                    for nextWord in nextWords:
                        if(nextWord != nodeWord):
                            if((nextWord in graph) and (nextWord not in graph[nodeWord])):
                                graph[nodeWord].append(nextWord)

                    
            dfsvisited[nodeWord] = 1       
            print(nodeWord,graph[nodeWord])
            
            adjNodes = graph[nodeWord]
            
            for adjNode in adjNodes:
                if(adjNode not in dfsvisited):
                    temp = result.copy()
                    temp.append(adjNode)
                
                    dfs(adjNode,temp)
                
                
            
        
        dfs(beginWord,[beginWord])
        
        print(ans)
        
        
        
        
            
                    
                    
                
                
                
            
        
        
        
        
        
        
        
        
        
        
			
        
        
        