#第六题：找Bug
#原代码：
# 第6行报错 list index out of range
#if __name__ == "__main__":
#    list = list(range(1000))
#    for idx in range(len(list)):
#        if list[idx] % 2 == 1:
#            list.pop(idx)
#问题：由于for函数先调用的list长度固定，后面list长度减少导致超限
if __name__ == "__main__":
    int_list = list(range(1000))
    new_list = []
    for idx in range(len(int_list)):
        if int_list[idx] % 2 == 0:
            new_list.append(int_list[idx])
    print(new_list)

