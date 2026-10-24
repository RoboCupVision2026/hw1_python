def read_number():
    try:
        text = input("请输入一个正整数: ").strip()
    except EOFError:
        text = ""
    if not text.isdigit() or int(text) == 0:
        print("没有输入有效正整数，改用示例数据: 12321")
        text = "12321"
    return text


def is_palindrome_by_string(text):
    return text == text[::-1]


def is_palindrome_by_math(number):
    reverse = 0
    rest = number
    while rest:
        reverse = reverse * 10 + rest % 10
        rest //= 10
    return reverse == number


def main():
    samples = [read_number(), "123321", "12345"]
    for text in samples:
        number = int(text)
        by_string = is_palindrome_by_string(text)
        by_math = is_palindrome_by_math(number)
        result = "是回文数" if by_string and by_math else "不是回文数"
        print(f"{number} {result}（字符串法: {by_string}，整数法: {by_math}）")


if __name__ == "__main__":
    main()
