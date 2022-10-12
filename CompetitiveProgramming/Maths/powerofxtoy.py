

def pow(x,y):

  if(x == 0 or x == 1):
    return x

  if(y == 0):
    return 1

  temp = pow(x,y//2)
  
  if (y % 2 == 0):
    return temp * temp 

  else:
    return x * temp * temp 


print(pow(3,4))
print(pow(5,4))
  
