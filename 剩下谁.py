a=list(range(1,234))
i=0
while len(a)>1:
    i=(i+2)%len(a)
    a.pop(i)
print("留下",a[0],"号",sep="")
