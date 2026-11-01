if __name__ == "__main__":
    lst = list(range(1000))
    lst = [x for x in lst if x % 2 == 0]
    print(lst)