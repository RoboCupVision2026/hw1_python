# ## 十四

with open("test.txt", "r", encoding="utf-8") as file:
    with open("copy_test.txt", "r", encoding="utf-8") as copy:
        n=1
        a= file.readline()
        b= copy.readline()
        while a != "" or b != "":
            if a != b:
                print("ciallo！！第",n,"行不一样哦！")
            a= file.readline()
            b= copy.readline()
            n= n + 1

