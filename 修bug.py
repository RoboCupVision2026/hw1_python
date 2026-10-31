if __name__ == "__main__":
    nums = list(range(1000))

    for idx in range(len(nums) - 1, -1, -1):
        if nums[idx] % 2 == 1:
            nums.pop(idx)

    print(nums)

#使用 pop(idx) 删除列表元素后，列表长度会减少，后续元素的索引也会向前移动。
#但 range(len(list)) 在循环开始时就确定了迭代范围，不会随着列表长度变化而更新。
#因此，循环继续执行时，可能访问不存在的索引，最终导致 IndexError: list index out of range。