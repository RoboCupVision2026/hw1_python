def main():
    x, y, z = map(int, input("请输入三个整数，以空格分隔：").split())
    print(*sorted([x, y, z]))


if __name__ == "__main__":
    main()
