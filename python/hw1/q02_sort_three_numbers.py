def read_numbers():
    try:
        text = input("请输入三个整数（空格或逗号分隔）: ")
    except EOFError:
        text = ""
    parts = text.replace(",", " ").split()
    if len(parts) != 3:
        print("没有输入三个整数，改用示例数据: 3 1 2")
        parts = ["3", "1", "2"]
    return int(parts[0]), int(parts[1]), int(parts[2])


def sort_by_swap(x, y, z):
    if x > y:
        x, y = y, x
    if x > z:
        x, z = z, x
    if y > z:
        y, z = z, y
    return x, y, z


def main():
    x, y, z = read_numbers()
    first, second, third = sort_by_swap(x, y, z)
    print(f"输入: x={x}, y={y}, z={z}")
    print(f"交换法由小到大输出: {first} {second} {third}")
    print(f"列表排序由小到大输出: {' '.join(str(value) for value in sorted([x, y, z]))}")


if __name__ == "__main__":
    main()
