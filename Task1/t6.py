#在一开始遍历的范围被确定，但列表越删越短，导致到后面越界；同时删除i位元素，后面一位向前递补成新的i位，这个元素就会被漏掉
#修改后的代码：
if __name__ == "__main__":
    list = list(range(1000))
    listp = list[:]
    for idx in range(len(listp)):
        if listp[idx] % 2 == 1:
            list.remove(listp[idx])