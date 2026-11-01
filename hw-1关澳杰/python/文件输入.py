import random
with open("numbers.txt","w",encoding="utf-8") as f:
    for i in range(10):
        a = random.randint(1,100)
        b = random.randint(1,100)
        c = random.randint(1,100)
        f.write(f"{a},{b},{c}\n")
with open("numbers.txt","r",encoding="utf-8") as f:
    line_list = []
    for line in f:
        line = line.strip()
        a,b,c = line.split(",")
        line_list.append(int(b))
    max = max(line_list)
    min = min(line_list)
    avg = sum(line_list)/len(line_list)
    line_list.sort()
    line_list2 = line_list
if(len(line_list2)%2==0):
    a = line_list2[len(line_list2)//2]
    b = line_list2[len(line_list2)//2-1]
    median = (a+b)/2
else:
    median = line_list[len(line_list)//2]
print(f"{max},{min},{avg},{median}")


