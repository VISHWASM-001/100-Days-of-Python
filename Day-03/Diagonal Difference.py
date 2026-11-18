def diagonalDifference(arr):
    left_to_right = 0
    right_to_left = 0
    for i in range(0,len(arr)):
        left_to_right += arr[i][i]  # 0 0,1 1,2 2
        
    for i in range(len(arr)):
        right_to_left += arr[i][len(arr)-i-1] # 0 2,1 1,2 0   
        
    return abs(left_to_right - right_to_left)  
