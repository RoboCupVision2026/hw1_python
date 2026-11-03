#问题：range(len(list))按原列表长度生成，不发生变化，后面删除元素后列表长度变短，会出现索引越界。我们倒序遍历列表即可解决问题。
#改进后代码如下
if __name__ == "__main__":
    list=list(range(1000))
    for idx in range(len(list)-1, -1, -1):
        if list[idx]%2==1:
            list.pop(idx)
    print(list)