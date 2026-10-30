# 找bug
# if __name__ == "__main__":
#     list = list(range(1000))
#     for idx in range(len(list)):
#         if list[idx] % 2 == 1:
            # list.pop(idx)
            
# bug：在运行过程中会删除list中的元素，导致list变短，报list index out of range的错误

# 修改后的代码为，改为了从后往前遍历：

if __name__ == "__main__":
    num = list(range(1000))
    for idx in range(len(num) - 1, -1, -1):
        if num[idx] % 2 == 1:
            num.pop(idx)
