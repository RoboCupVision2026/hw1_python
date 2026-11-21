""""
bug代码
if __name__ == "__main__":
    list = list(range(1000))
    for idx in range(len(list)):
        if list[idx] % 2 == 1:
            list.pop(idx)
"""

"""
错误原因：遍历的同时也在修改，导致 len 一直在变，从而使得部分元素遍历不到
"""

#改正代码：

if __name__ == "__main__":
    list = list(range(1000))
    list1 = list.copy()
    for idx in range(len(list)):
        if list[idx] % 2 == 1:
            list1.remove(list[idx])