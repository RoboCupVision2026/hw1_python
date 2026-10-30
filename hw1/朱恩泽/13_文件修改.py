def main():
    with open("test.txt", "r+", encoding="utf-8") as file:
        content = file.read()
        file.seek(0)
        file.write("python" + content + "python")
        file.truncate()


if __name__ == "__main__":
    main()
