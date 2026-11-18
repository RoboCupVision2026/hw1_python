if __name__ == "__main__":
    a = list(range(1000))
    a = [x for x in a if x % 2 == 0]
    print(a)
