"""
最后剩下谁

题目：有233个人围成一圈，顺序排号。从第一个人开始报数（从1到3报数），凡报到3的人退出圈子，问最后留下的是原来第几号的那位。

程序分析：利用列表和取余运算实现报数（列表内元素的循环），注意第五题的bug发生的原因。
"""

list = list(range(1, 234))
cnt = 0

while len(list) > 1:
    list1 = list.copy()

    for idx in range(len(list1)):
        cnt += 1
        if cnt == 3:
            list.remove(list1[idx])
            cnt = 0
            if len(list) == 1:
                break

print(list[0])
