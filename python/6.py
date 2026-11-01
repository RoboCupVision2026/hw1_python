if __name__ == "__main__":
    lst = list(range(1000))   # 原代码用list做变量名，list是内置函数，不建议，改成lst
    # 【BUG位置：原来的 for idx in range(len(lst)): 正向遍历】
    # 【BUG原因：range(len(lst)) 在循环一开始就一次性生成固定的索引序列，不会随着列表变短而更新。
    # 当 pop(idx) 删除一个元素，该位置后面所有元素全部向前移动一位，
    # 下一轮idx自增，就会跳过紧跟在被删除元素后面的那一个元素；
    # 循环到后面还会出现 idx 超过当前列表实际长度，从而越界。】
    # 修改方案：倒序遍历，从后往前删，前面元素前移不会影响还没遍历到的下标
    for idx in range(len(lst)-1, -1, -1):
        if lst[idx] % 2 == 1:
            lst.pop(idx)
    print(lst)
