# 第十四题：文件修改
# 题目：读取上题 test.txt 的文件内容，分别在文件的开头处和结尾处追加字符串 python。
# 思路：读入全部内容 -> 拼成 "python" + 原内容 + "python" -> 写回。

def add_python(path="test.txt"):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    new_content = "python" + content + "python"
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_content)
    return new_content


if __name__ == "__main__":
    result = add_python()
    print("修改后内容如下：")
    print(result)
