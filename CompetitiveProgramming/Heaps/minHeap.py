

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
        while(self.hasParent(index) and self.getParent(index) > self.a[index]):
            self.swap(self.getParentIndex(index),index)
            index = self.getParentIndex(index)

    def heapifyDown(self):
        index = 0
        while self.hasLeftChild(index):
            minChildIndex = self.getLeftChildIndex(index)
            if(self.hasRightChild(index) and self.getRightChild(index) < self.getLeftChild(index)):
                minChildIndex = self.getRightChildIndex(index)
            if(self.a[index] < self.a[minChildIndex]):
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

minHeap = MinHeap()
minHeap.insert(10)
minHeap.insert(2)
minHeap.insert(20)
minHeap.insert(5)

print(minHeap.a)


print(minHeap.pop())
print(minHeap.pop())

print(minHeap.a)



    

    

    


    

