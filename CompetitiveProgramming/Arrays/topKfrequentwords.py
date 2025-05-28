from collections import defaultdict, Counter
import heapq


class MinHeap:

    def __init__(self):
        self.a = []

    # Helper Methods
    def getParentIndex(self,index):
        return (index-1)//2
    
    def getLeftChildIndex(self,index):
        return 2*index+1
    
    def getRightChildIndex(self,index):
        return 2*index+2
    
    def hasParent(self,index):
        return self.getParentIndex(index)>=0
    
    def hasLeftChild(self,index):
        return self.getLeftChildIndex(index) <= len(self.a)-1
    
    def hasRightChild(self,index):
        return self.getRightChildIndex(index) <= len(self.a)-1
    
    def getParent(self,index):
        return self.a[self.getParentIndex(index)]

    def getLeftChild(self,index):
        return self.a[self.getLeftChildIndex(index)]

    def getRightChild(self,index):
        return self.a[self.getRightChildIndex(index)]
    
    def swap(self,index1,index2):
        temp = self.a[index2]
        self.a[index2] = self.a[index1]
        self.a[index1] = temp


    def heapifyUp(self):
        index = len(self.a) -1
        while(self.hasParent(index)):
            if self.getParent(index)[0] == self.a[index][0]:
                if self.getParent(index)[1] < self.a[index][1]:
                    self.swap(self.getParentIndex(index),index)
                    index = self.getParentIndex(index)
                else:
                    break
            elif self.getParent(index)[0] > self.a[index][0]:
                self.swap(self.getParentIndex(index),index)
                index = self.getParentIndex(index)
            else:
                break

    def heapifyDown(self):
        index = 0
        while self.hasLeftChild(index):
            minChildIndex = self.getLeftChildIndex(index)
            if(self.hasRightChild(index)):
                if self.getRightChild(index)[0] ==  self.getLeftChild(index)[0]:
                    if self.getRightChild(index)[1] > self.getLeftChild(index)[1]:
                        minChildIndex = self.getRightChildIndex(index)
                elif self.getRightChild(index)[0] <  self.getLeftChild(index)[0]:
                    minChildIndex = self.getRightChildIndex(index)

            if(self.a[index][0] < self.a[minChildIndex][0]):
                break

            elif (self.a[index][0] == self.a[minChildIndex][0]):
                if (self.a[index][1] > self.a[minChildIndex][1]):
                    break

            self.swap(index,minChildIndex)
            index = minChildIndex
    

    def insert(self,val):
        self.a.append(val)
        self.heapifyUp()

    def pop(self):
        if len(self.a) == 0:
            return None
        val = self.a[0]
        self.a[0] = self.a[len(self.a)-1]
        self.a.pop()
        self.heapifyDown()
        return val

class Solution:


    # Implementing using minHeap From Scratch
    def topKFrequent(self, words: List[str], k: int) -> List[str]:

        count = Counter(words)

        minHeap = MinHeap()

        for key,value in count.items():
            minHeap.insert([value,key])

            if len(minHeap.a) > k:
                minHeap.pop()

        result = []

        for x in range(len(minHeap.a)):
          
            val = minHeap.pop()
            result.insert(0,val[1])

        return result

    

    def topKFrequentHeapQ(self, words: List[str], k: int) -> List[str]:

        class MaxHeapStr(str):
            def __init__(self, string): self.string = string
            def __lt__(self,other): return self.string > other.string
            def __eq__(self,other): return self.string == other.string

        count = Counter(words)

        pq = []

        for key,value in count.items():
            heapq.heappush(pq,(value,MaxHeapStr(key)))

            if len(pq) > k:
                heapq.heappop(pq)

        result = []

        for x in range(len(pq)):
        
            val = heapq.heappop(pq)
            result.insert(0,val[1])

        return result





    # Using a priority Queue
    # Time Complexity : O(klogn)
    def topKFrequentHeapQ(self, words: List[str], k: int) -> List[str]:

        count = Counter(words)

        pq = []

        pq = [(-freq, word) for word, freq in count.items()]
        heapq.heapify(pq)

        return [heapq.heappop(pq)[1] for _ in range(k)]


    

    # Time Complexity : O(nlogn)
    def topKFrequentUsingBucketSort(self, words: List[str], k: int) -> List[str]:

        count = defaultdict(int)

        for word in words:
            count[word] += 1 

        n = len(words)

        bucket = [[] for i in range(n+1)]
        
        for key,value in count.items():

            bucket[value].append(key)

    
        result = []

        for i in range(n,0,-1):

            if len(bucket[i]) == 1:
                result.append(bucket[i][0])
                if len(result) == k:
                    return result
            else:
                tmp = bucket[i]
                tmp = sorted(tmp)
                for t in tmp:
                    result.append(t)
                    if len(result) == k:
                        return result

                




        