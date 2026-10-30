if __name__=="__main__":
    lst = list(range(1000))
    for idx in range(len(lst)-1,-1,-1):
        if lst[idx]%2==1:
            lst.pop(idx)
print(lst)
