people=list(range(233))
number=0
key=0
while len(people)!=1:
    if number==2:
        people.pop(key)
    else:
        key=(key+1)%len(people)
    number=(number+1)%3
print(people[0])