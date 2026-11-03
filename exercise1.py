num=0
for i in range(1,5):
    for j in range(1,5):
        if j!=i:
            for k in range(1,5):
                if k!=j and k!=i:
                    for z in range(1,5):
                        if z!=k and z!=j and z!=i:
                            num=i*1000+j*100+k*10+z
                            print(num)



