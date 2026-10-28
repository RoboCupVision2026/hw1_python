# 第十一题：最后剩下谁（约瑟夫环问题）
# 题目：233 个人围成一圈，顺序排号。从第一个人开始报数（从 1 报到 3），
#       凡报到 3 的人退出圈子，问最后留下的是原来第几号？
# 思路：用列表模拟活人，用一个游标 idx 数到 3 就把当前位置的人删掉。
#       注意列表删除后元素前移，用 idx = (idx + 2) % len(live) 来"数 3 步"。

def josephus(n, k):
    live = list(range(1, n + 1))   # 编号 1..n
    idx = 0
    while len(live) > 1:
        idx = (idx + k - 1) % len(live)   # 数到第 k 个
        live.pop(idx)                     # 淘汰
    return live[0]


if __name__ == "__main__":
    survivor = josephus(233, 3)
    print("233 人围成圈，报到 3 退出，最后剩下的是原第 {} 号".format(survivor))
