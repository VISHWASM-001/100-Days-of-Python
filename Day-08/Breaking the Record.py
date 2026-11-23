def breakingRecords(scores):
    minn = scores[0]
    maxx = scores[0]
    
    wellscored = 0
    downgrade = 0
    
    for i in range(1,len(scores)):
        if scores[i] > maxx:
            maxx = scores[i]
            wellscored+=1
        elif scores[i] < minn:
            minn = scores[i]
            downgrade += 1
        else:
            pass
    
    
    return wellscored,downgrade            
                
