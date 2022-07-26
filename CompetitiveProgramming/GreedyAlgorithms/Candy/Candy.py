class Solution:
    
    def candy2(self, ratings):
        
        candies = []
        
        candies.append(1)

        for i in range(1,len(ratings)):
            
            if(ratings[i]<ratings[i-1]):
                
                candies.append(1)
                
                while( i > 0 and ratings[i-1] > ratings[i] and candies[i-1] == candies[i]):
                   
                    candies[i-1] += 1
                    i-=1
                
            elif(ratings[i]>ratings[i-1]):
                candies.append(candies[i-1]+1)
                
            else:
                candies.append(1)
        
     
                
        return sum(candies)
    
    def candy(self,ratings):
        candies = []
        
        for i in range(len(ratings)):
            candies.append(1)
            
            
        for i in range(1,len(ratings)):
            if(ratings[i]>ratings[i-1]):
                candies[i] = candies[i-1]+1
              
        result = candies[len(ratings)-1]
        
        for i in range(len(ratings)-2,-1,-1):
            if(ratings[i]>ratings[i+1]):
                candies[i] = max(candies[i],candies[i+1]+1)
                print(candies[i])
            result += candies[i]
            
        return result
            
            
            
            