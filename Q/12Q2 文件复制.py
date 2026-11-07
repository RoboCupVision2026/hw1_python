import random as rd
def pp():
    return chr(rd.randint(32,126))

n=int(input("请输入行数"))
with open("test.txt","w",encoding="ascii") as f:
    for _ in range(n):
        num=rd.randint(1,20)
        line=''.join(pp() for _ in range(num))
        f.write(f"{line}\n")

with open("test.txt","r",encoding="ascii") as f1, open("copy_test.txt","w",encoding="ascii") as f2:
    inn=f1.read()
    f2.write(inn)
print('over')