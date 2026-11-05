# ## 十二

import random
with open("test.txt","w",encoding="utf-8")as file:
    i= int(input("几行？")) 
    for n in range(i):
        for x in range(30):
            num= random.randint(32,126)
            c= chr(num)
            file.write(c)
        file.write("\n")   
with open("test.txt","r",encoding="utf-8")as file:  
    text= file.read()  
with open("copy_test.txt","w",encoding="utf-8") as copy:
    copy.write(text)
print("ok了")    
             

