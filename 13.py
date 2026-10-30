prefix = "python"
suffix = "python"
with open('test.txt', 'r', encoding='utf-8') as f:
    content = f.read()
content = prefix + content + suffix
with open('test.txt', 'w', encoding='utf-8') as f:
    f.write(content)
print("已追加")