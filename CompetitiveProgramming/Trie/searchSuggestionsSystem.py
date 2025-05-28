from collections import defaultdict
import heapq

class Solution:
    
    # Using Trie
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:

        class TrieNode:

            def __init__(self):
                self.children = {}                
                self.suggestedWords = []

            def addSuggestions(self,word):
                heapq.heappush(self.suggestedWords,word)
                

            def getSuggestions(self):
                result = []
                t = len(self.suggestedWords) if len(self.suggestedWords)<3 else 3
                for i in range(t):
                    result.append(heapq.heappop(self.suggestedWords))
                return result
            
            # def addSuggestions(self,word):
            #     if len(self.suggestedWords) < 3:
            #         heapq.heappush(self.suggestedWords,MaxHeapStr(word))
            #     else:
            #         heapq.heappush(self.suggestedWords,MaxHeapStr(word))
            #         heapq.heappop(self.suggestedWords)

            # def getSuggestions(self):
            #     result = []
            #     for i in range(len(self.suggestedWords)):
            #         result.insert(0,heapq.heappop(self.suggestedWords))
            #     return result


        # class MaxHeapStr(str):
        #     def __init__(self, string): self.string = string
        #     def __lt__(self,other): return self.string > other.string
        #     def __eq__(self,other): return self.string == other.string
        

        root = TrieNode()

        for product in products:
            curr = root

            for ch in product:
                if ch not in curr.children:
                    curr.children[ch]  = TrieNode()

                curr = curr.children[ch]
                curr.addSuggestions(product)

        results = []
        curr = root

        for i,ch in enumerate(searchWord):
            if ch in curr.children:
                curr = curr.children[ch]
                results.append(curr.getSuggestions())
            else:
                for _ in range(len(searchWord)-i):
                    results.append([])
                break

        return results



    # Time Complexity 
    # Sorting : O(nlogn)
    # Filtering : O(nm)
    def suggestedProducts2(self, products: List[str], searchWord: str) -> List[List[str]]:

        products = sorted(products)

        results = []

        filteredWords = []

        for i in range(len(searchWord)):
            searchString = searchWord[0:i+1]

            if len(filteredWords) == 0:
                for product in products:
                    if(product.startswith(searchString)):
                        filteredWords.append(product)
                results.append(filteredWords if len(filteredWords) == 3 else filteredWords[0:3])
            else:
                temp = []
                for product in filteredWords:
                    if(product.startswith(searchString)):
                        temp.append(product)
                results.append(temp if len(temp) == 3 else temp[0:3])
                filteredWords = temp

        return results
                

            
        