def queue(n=233,m=3):
    people=list(range(1,n+1))
    idx=0
    while len(people)>1:
        idx=(idx+m-1)%len(people)
        people.pop(idx)
    return people[0]
result =queue(233,3)
print(f"最后留下的原来第{result}号")