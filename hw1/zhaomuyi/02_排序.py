# 第二题：排序
# 题目：输入三个整数 x, y, z，请把这三个数由小到大输出。
# 思路：法二——放进列表，直接调用 list.sort()，最简洁。

def sort_three(a, b, c):
    lst = [a, b, c]
    lst.sort()
    return lst


if __name__ == "__main__":
    x = int(input("请输入第一个整数 x: "))
    y = int(input("请输入第二个整数 y: "))
    z = int(input("请输入第三个整数 z: "))
    result = sort_three(x, y, z)
    print("从小到大排序为：", result)
