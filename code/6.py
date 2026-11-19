# 找 bug
if __name__ == "__main__":
    list = list(range(1000))
    for idx in range(len(list) - 1, -1, -1): # range 只在一开始生成，但 list 每次 pop 后都会使 list 总长变短，最终 idx 超过 list 的总长导致越界
        if list[idx] % 2 == 1:
            list.pop(idx)
# print(*list)