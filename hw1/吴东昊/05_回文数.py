n=input("正整数：").strip().lstrip("0")
print("回文数" if n==n[::-1] else "非回文数")
