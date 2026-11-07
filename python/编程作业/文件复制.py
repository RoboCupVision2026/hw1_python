import random
lines = int(input("请输入要生成的行数: "))
with open("test.txt", "w") as f:
    for i in range(lines):
        length = random.randint(10, 20)
        line_c = ""
        for j in range(length):
            line_c += chr(random.randint(32, 126))
        f.write(line_c + "\n")
with open("test.txt", "r") as f_read:
    c = f_read.read() 
with open("copy_test.txt", "w") as f_write:
    f_write.write(c)  
