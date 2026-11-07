with open("test.txt","r",encoding="ascii") as f:
    inn = f.read().rstrip()
    inn2 = 'python' + inn + 'python\n'
with open("test.txt","w",encoding="ascii") as f:
    f.write(inn2)
print('over')