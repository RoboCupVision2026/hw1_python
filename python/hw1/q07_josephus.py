def last_remaining(total, step):
    people = list(range(1, total + 1))
    index = 0
    round_number = 1
    while len(people) > 1:
        index = (index + step - 1) % len(people)
        out = people.pop(index)
        if round_number <= 5:
            print(f"第 {round_number} 个退出的是 {out} 号，剩 {len(people)} 人")
        round_number += 1
    return people[0]


def main():
    total = 233
    step = 3
    print(f"{total} 个人围成一圈，从 1 开始报数，报到 {step} 的退出")
    winner = last_remaining(total, step)
    print(f"一共退出 {total - 1} 人")
    print(f"最后剩下的是原来第 {winner} 号的那位")


if __name__ == "__main__":
    main()
