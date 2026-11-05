import random
# ## 十五
# ### 把前面的一起再来一遍？

from pathlib import Path
f= Path.cwd() / "test"
f.mkdir(exist_ok=True)

x=int(input("几个"))
y=int(input("几行"))

for i in range(x):
    n= str(i + 1) + ".txt"
    with open(f/n, "w", encoding="utf-8") as file:
         for q in range(y): 
            for z in range(30):
                num= random.randint(32,126)
                c= chr(num)
                file.write(c)
            file.write("-python\n")
    new= str(i + 1) + "-python.txt"
    (f / n).rename(f / new) 
    
print("好了好了累死我了")    

