# 第一题：组成三位数
# 题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
# 思路：百位、十位、个位分别从 {1,2,3,4} 里选，用三重循环，
#       再用 if 保证三个位置的数字互不相同。

results = []
for bai in [1, 2, 3, 4]:        # 百位
    for shi in [1, 2, 3, 4]:    # 十位
        for ge in [1, 2, 3, 4]: # 个位
            if bai != shi and bai != ge and shi != ge:
                num = bai * 100 + shi * 10 + ge
                results.append(num)

print("能组成的三位数共有 {} 个：".format(len(results)))
print(results)
