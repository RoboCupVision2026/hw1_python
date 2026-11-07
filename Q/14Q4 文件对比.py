with open('test.txt','r',encoding = 'utf-8') as f1, open('copy_test.txt','r',encoding = 'utf-8') as f2:
    l1 = f1.readlines()
    l2 = f2.readlines()
    ln = min(len(l1),len(l2))
    for i in range(ln):
        if l1[i] != l2[i]:
            print(f'第{i+1}行不一样')
print('over')