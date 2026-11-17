def plusMinus(arr):
    positive = 0
    negative = 0
    zeros = 0
    
    for i in arr:
        if i > 0:
            positive+=1
        elif i < 0:
            negative +=1
        else:
            zeros+=1
            
    print(f"{positive/len(arr):.6f}")                 
    print(f"{negative/len(arr):.6f}")                 
    print(f"{zeros/len(arr):.6f}")                 
   
