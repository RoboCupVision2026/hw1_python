num=int(input())
numm=int(str(num)[::-1])
if num==numm:
    print("This number is a palindrome")
else:
    print("This number is not a palindrome")