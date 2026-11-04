n=233
m=3
people=list(range(1,n+1))
pos=0
while len(people)>1:
    pos=(pos+m-1)%len(people)
    people.pop(pos)
print(people[0])