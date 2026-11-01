if __name__ == "__main__":
    n = 233
    people = list(range(1, n+1))
    idx = 0
    while len(people) > 1:
        idx = (idx + 2) % len(people)
        people.pop(idx)
    print("最后剩下的编号：", people[0])
