def main():
    people = list(range(1, 234))
    index = 0
    while len(people) > 1:
        index = (index + 2) % len(people)
        people.pop(index)
    print(people[0])


if __name__ == "__main__":
    main()
