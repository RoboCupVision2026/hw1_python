i=0
for a in range(1,5,1):
    for b in range(1,5,1):
        if a==b :
            continue
        else:
            for c in range(1,5,1):
                if a==c:
                    continue
                elif b==c:
                    continue
                else:
                    for d in range(1,5,1):
                        if a==d:
                            continue
                        elif b==d:
                            continue
                        elif c==d:
                            continue
                        else :
                            i+=1
                            print(a*1000+b*100+c*10+d)
print(i)                           
            
        
