'''
原程序：
if __name__ =="__main__":
    list = list(range(1000))
    for idx in range(len(list)):
        if list[idx] % 2 ==1:
            list.pop(idx)
问题：
    1.一边循环一边删除list的元素，删除元素后列表长度变短，i就会超出原长度
    2.list作为变量名不合适
'''
if __name__=="__main__":
    lst = list(range(1000))
    for idx in range(len(lst)-1,-1,-1):
        if lst[idx] %2 == 1:
            lst.pop(idx)