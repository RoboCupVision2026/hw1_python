# 第五题：文件改名
#
# 题目：在上一题的基础上，随机将 50 个文件改名为以 .jpg 结尾。
from pathlib import Path
import random
old_path = Path(__file__).resolve().parent/"img"
s_1 = old_path.glob("*.png")
s1 = list(s_1)
s2 = random.sample(s1,50)
for i in s2:
    new=i.with_suffix(".jpg")
    i.rename(new)

