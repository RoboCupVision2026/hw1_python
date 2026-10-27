l=list(range(1,234))
idx=2
while True:
    l.pop(idx)
    idx=(idx+2)%len(l)
    if len(l)==1:
        break
print(l[0])

