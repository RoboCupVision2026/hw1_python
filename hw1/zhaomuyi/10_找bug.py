# 第十题：找 bug
# 题目：下面这段代码的目的是把 list 中所有的奇数删除，但它无法运行。
#       请找出 bug 在哪、为什么会发生，并改正。
#
# 【原始有 bug 的代码】
# if __name__ == "__main__":
#     list = list(range(1000))
#     for idx in range(len(list)):
#         if list[idx] % 2 == 1:
#             list.pop(idx)
#
# 【Bug 分析】
# Python 的 list 是可变对象：每 pop(idx) 删一个元素，列表长度会缩短 1，
# 后面的元素会整体往前挪一位。但循环里 idx 是从 range(len(list)) 算出来的、
# 一开始就固定好了（range 只取一次长度），于是会出现两个问题：
#   1) IndexError：pop 几次之后，列表真实长度 < idx，再 list[idx] 就越界报错；
#   2) 即使不报错，元素前移后，下一个奇数会被"跳过"（因为它现在变成了 idx-1 的位置，
#      而循环已经走到 idx+1 了），导致删不干净。
#
# 【改正方法】
# 方法一（推荐）：不要边遍历边删原列表，改用列表推导式重建一个新列表，最直观安全。
# 方法二：从后往前遍历删除，这样前面元素的索引不受影响。

if __name__ == "__main__":
    lst = list(range(1000))

    # 改正后：列表推导式，只保留偶数
    even = [x for x in lst if x % 2 == 0]
    print("原列表长度：", len(lst))
    print("删除所有奇数后，剩下偶数的个数：", len(even))
    print("前 10 个偶数：", even[:10])

    # --- 另一种写法（从后往前 pop），作为对比 ---
    lst2 = list(range(20))
    for i in range(len(lst2) - 1, -1, -1):
        if lst2[i] % 2 == 1:
            lst2.pop(i)
    print("从后往前删奇数结果：", lst2)
