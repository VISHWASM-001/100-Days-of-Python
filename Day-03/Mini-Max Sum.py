# apprach 1
# using all inbuilt methods
def miniMaxSum(arr):
    sum1 = sum(arr)
    
    min_value = sum1 - max(arr)
    max_value = sum1 - min(arr)
    
    print(f"{min_value} {max_value}") 

# approach 2
# loopp after sorting 
def minimax(arr):
  arr.sort()
  min , max = 0,0
  for i in range(1,len(arr)):
    min += arr[i]

  for j in range(len(arr)-1):
    max += arr[j]


  
