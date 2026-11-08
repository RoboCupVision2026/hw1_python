fib=[0,1]
for i in range(1,19):
    fib.append(fib[i-1]+fib[i])
print(fib)
