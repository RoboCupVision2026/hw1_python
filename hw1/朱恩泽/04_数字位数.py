def main():
    number = int(input("请输入正整数："))
    if number <= 0:
        raise ValueError("请输入正整数")
    digits = str(number)
    print(len(digits))
    print(*digits[::-1])


if __name__ == "__main__":
    main()
