def main():
    print("用 list 作变量名会遮蔽内置类型，应改用其他名称。")
    print("正序删除会使元素前移、列表缩短，造成漏检和索引越界，应倒序删除。")
    numbers = list(range(1000))
    for index in range(len(numbers) - 1, -1, -1):
        if numbers[index] % 2 == 1:
            numbers.pop(index)
    print(numbers)


if __name__ == "__main__":
    main()
