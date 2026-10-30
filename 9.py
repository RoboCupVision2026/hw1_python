import os
from string import ascii_uppercase,digits
base_dir = os.path.dirname(os.path.abspath(__file__))
img_dir = os.path.join(base_dir, 'img')
os.makedirs(img_dir, exist_ok=True)
chars=ascii_uppercase + digits
used = set()
count=0
import random
while count<100:
    name = ''.join(random.choice(chars) for _ in range(4)) + '.png'
    if name not in used:
        used.add(name)
        open(os.path.join(img_dir, name), 'w').close()
        count += 1
print('文件创建完成')