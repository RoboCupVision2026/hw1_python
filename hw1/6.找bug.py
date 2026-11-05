if __name__=="__main__":
    list=list(range(1000))
    for idx in range(len(list)-1,-1,-1):
        #从后往前遍历，后面的元素被删除就不会影响到前面元素的索引序号
        if list[idx]%2==1:
            list.pop(idx)
            #删元素会导致列表变短，后面的索引就越界了
    print(list)