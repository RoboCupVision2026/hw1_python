# ## 第五题:回文数

number= input("正整数哦")
b= number[::-1]
if number == b:
    print ("是回文数哦")
else:
    print("人家才不是回文数呢")
