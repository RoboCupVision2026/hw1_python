def main():
    number = int(input("请输入正整数："))
    if number <= 0:
        raise ValueError("请输入正整数")
    digits = str(number)
    print("是回文数" if digits == digits[::-1] else "不是回文数")


if __name__ == "__main__":
    main()
