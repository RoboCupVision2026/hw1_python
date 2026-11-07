n = int(input())
origin = n    
reverse = 0


while n > 0:
    digit = n % 10
    reverse = reverse* 10 + digit
    n = n // 10


if origin == reverse:
    print("是回文数")
else:
    print("不是回文数")
