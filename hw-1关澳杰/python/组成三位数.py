total = 0
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if(i!=j and k!=j and k!=i):
                print(i*100 + j*10 + k)
                total += 1
print(total)