import os
import random
base_dir=os.path.dirname(os.path.abspath(__file__))
file_dir=os.path.join(base_dir,"img/")
count=0
while True:
    s=random.randint(1,100)
    if os.path.exists(file_dir+str(s)+'.jpg'):
            continue
    else:
          os.rename(file_dir+str(s)+'.txt',file_dir+str(s)+'.jpg')
          count+=1
    if count==50:
        break
    
   