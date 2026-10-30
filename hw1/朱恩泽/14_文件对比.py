from itertools import zip_longest


def main():
    with open("test.txt", encoding="utf-8") as original:
        with open("copy_test.txt", encoding="utf-8") as copied:
            for line_number, (left, right) in enumerate(
                zip_longest(original, copied), start=1
            ):
                if left != right:
                    print(line_number)


if __name__ == "__main__":
    main()
