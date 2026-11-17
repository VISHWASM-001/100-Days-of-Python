#approach 1
def compareTriplets(a, b):
    alice = 0
    bob = 0
    for i in range(0,len(a)):
        if a[i] > b [i]:
            alice += 1
        elif a[i] == b[i]:
            pass
        else:
            bob+=1
            
    return [alice,bob]      
  
#approach 2    
def compareTriplets(a, b):
    alice = 0
    bob = 0

    for x, y in zip(a, b):
        if x > y:
            alice += 1
        elif x < y:
            bob += 1

    return [alice, bob]  
               
