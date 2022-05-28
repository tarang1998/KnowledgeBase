#https://www.codingninjas.com/codestudio/problems/975277?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website&leftPanelTab=1

def findMinimumCoins(amount):
    
    denominations = [1, 2, 5, 10, 20, 50, 100, 500, 1000]
    
    n = len(denominations)
    
    remainingAmount = amount 
    
    noOfCoins = 0
    
    for i in range(n-1,-1,-1):
        
        if(remainingAmount >= denominations[i]):
            
            k = remainingAmount//denominations[i]
            
            remainingAmount -= denominations[i]*k
            
            noOfCoins += k
            
        if(remainingAmount == 0 ):
            
            break
        
    return noOfCoins
    