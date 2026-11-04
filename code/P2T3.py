n=int(input("please enter a positive integer:"))
a=n
digits=0
while a>0:
    a=a//10
    digits+=1
print(f"It's a {digits}-digit number.")
a=n
while a>0:
    print(a%10,end="")
    a=a//10
print()