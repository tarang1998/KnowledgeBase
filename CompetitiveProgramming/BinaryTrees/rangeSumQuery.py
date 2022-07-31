# https://leetcode.com/problems/range-sum-query-mutable/

class NumArray:
    
    tree = None
    n = 0

    def __init__(self, nums: List[int]):
        
        self.n = len(nums)
        
        self.tree = [0] * self.n * 2
        
        j = 0 
        
        for i in range(self.n,2*self.n):
            
            self.tree[i] = nums[j]
            
            j+=1
            
        for i in range(self.n-1,0,-1):
            
            self.tree[i] = self.tree[i*2] + self.tree[i * 2 + 1]
            
        print(self.tree)
            
            
            
        

    def update(self, index: int, val: int) -> None:
        pos = index + self.n
        self.tree[pos] = val
        
        while(pos > 0):
            
            left = pos
            right = pos
            
            if(pos % 2 == 0 ):
                right +=1 
            else:
                left -= 1
                
                
            self.tree[pos//2] = self.tree[left] + self.tree[right]
            pos = pos//2
            
            
            
        

    def sumRange(self, left: int, right: int) -> int:
        
        left += self.n
        right += self.n
        
        result = 0 
        
        while(left<=right):
            
            if((left%2) == 1):
                result += self.tree[left]
                left+=1
                
            if((right%2)== 0):
                result += self.tree[right]
                right-=1
                
            left = left//2
            right = right//2
            
        return result
                
            
        
        
        
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)