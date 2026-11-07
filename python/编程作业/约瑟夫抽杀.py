total =233

people =[0]*total 

count =0      
remain= total 
now = 0         

while remain > 1: 
    if people[now] == 0:
        count += 1       
        if count == 3:   
            people[now] = 1  
            count = 0       
            remain= remain-1   
            
    now += 1         
    if now == total: 
        now = 0      
for i in range(total):
    if people[i] == 0:
        print(i+1)
