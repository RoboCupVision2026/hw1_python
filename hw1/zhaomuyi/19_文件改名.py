# 第十九题：文件改名
# 题目：在上一题（img 目录里 100 个 .png 文件）的基础上，
#       随机将其中 50 个文件改名为 .jpg 结尾。

import os
import random


def rename_half(folder="img", change_count=50):
    files = [f for f in os.listdir(folder) if f.endswith(".png")]
    chosen = random.sample(files, change_count)
    for name in chosen:
        old = os.path.join(folder, name)
        new = os.path.join(folder, name[:-4] + ".jpg")
        os.rename(old, new)
    print("已随机将 {} 个 .png 改名为 .jpg".format(change_count))


if __name__ == "__main__":
    # 先跑一下第 18 题建目录，再改名（保证脚本单独运行也能出结果）
    import importlib.util
    spec = importlib.util.spec_from_file_location(
        "q18", os.path.join(os.path.dirname(__file__), "18_创建顺序文件.py"))
    q18 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(q18)
    q18.make_img_dir()

    rename_half()
