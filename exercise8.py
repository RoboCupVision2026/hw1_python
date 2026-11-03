import random
import os
base_dir = os.path.dirname(os.path.abspath(__file__))
data_file = os.path.join(base_dir, "data.txt")
with open(data_file,"w",encoding="utf-8") as f:
    for i in range(1,100001):
        f.write(str(random.randint(1,100)) + "\n")