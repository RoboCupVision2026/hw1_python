x=int(input("請輸入一個整數: "))
y=int(input("請輸入另一個整數: "))
z=int(input("請輸入第三個整數: "))
if x>y:
    x, y=y, x
if x>z:
    x, z=z, x
if y>z:
    y, z=z, y
print("從小到大：", x, y, z)