def buggy_version(data):
    for idx in range(len(data)):
        if data[idx] % 2 == 1:
            data.pop(idx)
    return data


def fix_backward(data):
    for idx in range(len(data) - 1, -1, -1):
        if data[idx] % 2 == 1:
            data.pop(idx)
    return data


def fix_comprehension(data):
    return [value for value in data if value % 2 == 0]


def fix_while(data):
    idx = 0
    while idx < len(data):
        if data[idx] % 2 == 1:
            data.pop(idx)
        else:
            idx += 1
    return data


def fix_slice(data):
    return data[::2]


def main():
    print("题目代码：")
    print("  if __name__ == '__main__':")
    print("      list = list(range(1000))")
    print("      for idx in range(len(list)):")
    print("          if list[idx] % 2 == 1:")
    print("              list.pop(idx)")
    print()
    print("bug 在哪：")
    print("  1. range(len(list)) 只在循环开始时算一次长度，随后 list.pop 让列表变短，")
    print("     索引仍然走到原来的上限，于是 list[idx] 越界，抛出 IndexError。")
    print("  2. 删除元素后后面的元素整体前移一位，下一次循环 idx 加 1 会跳过紧邻的那个元素，")
    print("     即使不报错也会漏删奇数。")
    print("  3. 列表是可变对象，循环里修改它的长度，下标与元素的一一对应关系就被破坏，")
    print("     而 range 生成的下标序列是固定的，不跟着变。")
    print()

    try:
        buggy_version(list(range(1000)))
    except Exception as error:
        print(f"运行原代码的结果: {type(error).__name__}: {error}")
    print()

    original = list(range(1000))
    for name, fixed in [
        ("倒序删除", fix_backward(list(original))),
        ("列表推导式", fix_comprehension(list(original))),
        ("while 修正下标", fix_while(list(original))),
        ("切片取偶数位", fix_slice(list(original))),
    ]:
        print(f"{name}: 剩余 {len(fixed)} 个元素，全是偶数: {all(v % 2 == 0 for v in fixed)}，前 5 个: {fixed[:5]}")


if __name__ == "__main__":
    main()
