with open('test.txt', 'r', encoding='utf-8') as f:
    content = f.read()

new_content = "python" + content + "python"

with open('test.txt', 'w', encoding='utf-8') as f:
    f.write(new_content)