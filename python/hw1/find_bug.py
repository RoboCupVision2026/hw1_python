#list.pop(idx)命令会改变list的长度，导致idx取值会大于列表索引最大值出现报错
if __name__ == "__main__":
    list=list(range(1000))
    list2=[]
    for idx in range(len(list)):
        if list[idx] %2!=1:
            list2.append(list[idx])
    list=list2