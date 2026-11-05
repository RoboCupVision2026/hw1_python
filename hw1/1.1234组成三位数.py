cnt=0
for i in range(1,5):
    for j in range(1,5):
        if not j==i:
            for k in range(1,5):
                if not k==i and not k==j:
                    print(i,j,k,sep="",end=" ")
                    cnt+=1
print(f"\n一共能组成{cnt}个三位数，分别如上。")