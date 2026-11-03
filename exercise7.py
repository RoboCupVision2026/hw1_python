num=list(range(1,234))
x=0
while len(num)>1:
   x=(x+2)%len(num)
   num.pop(x)
print(num[0])
 