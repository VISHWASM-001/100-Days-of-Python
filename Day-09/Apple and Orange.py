def countApplesAndOranges(s, t, a, b, apples, oranges):
    a_count = 0
    b_count = 0
    
    for i in apples:
        if i+a >= s and i+a <= t:
            a_count += 1
        
    for i in oranges:
        if i+b >= s and i+b <= t:
            b_count += 1 
    
    print(a_count)
    print(b_count) todays 100days challenge
