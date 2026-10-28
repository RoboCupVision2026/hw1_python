def main():
    digits = [1, 2, 3, 4]
    numbers = []
    for a in digits:
        for b in digits:
            for c in digits:
                if a != b and b != c and a != c:
                    numbers.append(a * 100 + b * 10 + c)
    print(f"用 1、2、3、4 能组成 {len(numbers)} 个互不相同且无重复数字的三位数：")
    for start in range(0, len(numbers), 8):
        print("  ".join(str(number) for number in numbers[start:start + 8]))


if __name__ == "__main__":
    main()
