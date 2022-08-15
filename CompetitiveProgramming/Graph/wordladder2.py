from collections import deque, defaultdict 

class Solution:
    
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        
        #if end word not in list return []
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
        nodelevel = defaultdict(list)
        
        bfsqueue = [(endWord,0)]
        visited[endWord] = 1
        
        while(len(bfsqueue) != 0):
            
            wordNode = bfsqueue.pop(0)
            
            ele = wordNode[0]
            level = wordNode[1]
            nodelevel[level].append(ele)
            
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
                        bfsqueue.append((nextWord,level+1))
              
                            
        #Backtracking from the beginning Word
    
    
        def dfs(nodeWord,result,level):
            
            if(nodeWord == endWord):
                ans.append(result)
                return
            
            nodesInPreviousLevel = nodelevel[level-1]
            possibleNodesInPreviousLevel = []
            
            
            for i in range(len(nodeWord)):

                nextWordPattern = nodeWord[:i]+"*"+nodeWord[i+1:]

                nextWords = d[nextWordPattern]
                possibleNodesInPreviousLevel.extend(nextWords)
                    
                    

            for i in nodesInPreviousLevel:
                if(i in possibleNodesInPreviousLevel and i not in graph[nodeWord]):
                    
                    graph[nodeWord].append(i)
                    graph[i].append(nodeWord)
                    
     
            
            adjNodes = graph[nodeWord]
            
            for adjNode in adjNodes:
                if(adjNode in nodelevel[level-1]):
                    temp = result.copy()
                    temp.append(adjNode)
                
                    dfs(adjNode,temp,level-1)
                
                
            
        
        dfs(beginWord,[beginWord],len(nodelevel)-1)
        
        return ans
        
        
        
        
            
                    
                    
                
                
                
            
        
        
        
        
        
        
        
        
        
        
			
        
        
        