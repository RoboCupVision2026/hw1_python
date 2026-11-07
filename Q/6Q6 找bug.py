#bug：当pop掉列表的元素的时候，列表变短；但是len(lst)已经计算 idx所遍历的值不会变 于是会超过列表的索引
# if __name__=="__main__":
#     lst =list(range(1000))
#     for idx in range(len(lst)):
#         if lst[idx]%2==1:
#             lst.pop(idx)
if __name__=="__main__":
    lst =list(range(1000))
    idx=0
    while idx<len(lst):
        if lst[idx]%2==1:
            lst.pop(idx)
        else:
            idx+=1
#    print(*lst)