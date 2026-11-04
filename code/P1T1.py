a=0
for i in[1,2,3,4]:
    for j in[1,2,3,4]:
        for k in[1,2,3,4]:
            if i!=j and j!=k and k!=i:
                num=i*100+j*10+k
                print(num)
                a+=1
print(f"Total:{a}")