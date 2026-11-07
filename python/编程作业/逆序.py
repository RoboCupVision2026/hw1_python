n = int(input())


temp = n       
count = 0
while temp > 0:
        count =count +1
        temp = temp // 10  
print("位数:", count)

temp = n       
print("逆序打印: ", end="") 

while temp > 0:
    digit = temp % 10  
    print(digit, end="")
    temp = temp // 10  

print() 
