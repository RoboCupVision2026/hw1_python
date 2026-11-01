# 这个程序最大的问题就是没有考虑到在循环中删除元素后列表本身也会改变
# 如果要通过循环来删除，倒着删

if __name__ == "__main__":
    result = list(range(1000))
    idx = len(result) - 1
    while idx >= 0:
        if result[idx] % 2 == 1:
            result.pop(idx)
        idx -= 1
    print(result)
