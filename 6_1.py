# bug: 正序删除会使列表变短、后面的元素前移，下标全部减1，list的长度会减少，但是range(len(list))用
# 的是一开始list的长度，这会导致越界访问，程序无法正常运行
# 而且也没办法删除所有奇数位置的元素。
# 解决方法：改成倒序遍历，删除元素就不会影响接下来要访问的下标。

numbers = list(range(1000))

for idx in range(len(numbers) - 1, -1, -1):
    if numbers[idx] % 2 == 1:
        numbers.pop(idx)

print("删除奇数后的列表：")
print(numbers)
