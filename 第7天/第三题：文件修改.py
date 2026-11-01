# 读取test.txt，并在文件的开头和结尾处追加字符串python
# 但是使用seek(0)进行write会覆盖原有的字符，所以只能全部读取出来进行改写后覆盖源文件
with open("generatedFiles/test.txt", 'r', encoding='utf-8') as f:
    content = f.read()

newContent = "python" + content + "python"

with open("generatedFiles/test.txt", 'w', encoding='utf-8') as f:
    f.write(newContent)