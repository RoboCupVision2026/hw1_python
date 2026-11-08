#pop使列组元素减少,从而导致正序寻找时列组错位，并且有越界风险
#以下为更改后的代码
if __name__=="__main__":
    list=list(range(1000))
    for i in range(len(list)-1,0,-1):
        if list[i]%2==1:
            list.pop(i)
    print(list)



