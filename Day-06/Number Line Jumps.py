def kangaroo(x1, v1, x2, v2):
    
    initial_distance = x2 - x1;
    
    Speed_difference = v1 - v2;
    
    if v1 > v2 and initial_distance%Speed_difference == 0:
        return "YES"
    
    return "NO"  
