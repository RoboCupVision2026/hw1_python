def read_number():
    try:
        text = input("请输入一个正整数: ").strip()
    except EOFError:
        text = ""
    if not text.isdigit() or int(text) == 0:
        print("没有输入有效正整数，改用示例数据: 12345")
        text = "12345"
    return text


def count_digits(number):
    total = 0
    while number:
        total += 1
        number //= 10
    return total


def split_digits(number):
    digits = []
    while number:
        digits.append(number % 10)
        number //= 10
    return digits


def main():
    text = read_number()
    number = int(text)
    print(f"输入的正整数: {number}")
    print(f"它是 {count_digits(number)} 位数")
    print(f"整数法逐位分解: {' '.join(str(digit) for digit in split_digits(number))}")
    print(f"逆序打印各位数字: {' '.join(reversed(text))}")
    print(f"逆序后的整数: {int(text[::-1])}")


if __name__ == "__main__":
    main()
