#第二题：排序
#题目：输入三个整数x,y,z，请把这三个数由小到大输出。
#程序分析：
#法一：我们想办法把最小的数放到x上。先将x与y进行比较，如果x>y则将x与y的值进行交换，
#然后再用x与z进行比较，如果x>z则将x与z的值进行交换，这样能使x最小。
#法二：将x、y、z组成一个列表，然后对列表进行排序。

x = int(input())
y = int(input())
z = int(input())

#sol1
if x > y:
    x, y = y, x
if x > z:
    x, z = z, x
if y > z:
    y, z = z, y
print(x, y, z)

#sol2
num = [x, y, z]
num.sort()
print(num[0], num[1], num[2])