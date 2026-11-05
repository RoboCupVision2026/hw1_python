# ## 第六题：找bug
# ### 问题在于他把索引从前向后添加，导致删除数字后，数组自动前移，补齐位置，不仅少检查了数，到最后检查到空索引还会报错。然后命名时list已经被占用

numbers= list(range(1000))
for idx in range(len(numbers) - 1, -1, -1):
    if numbers[idx] % 2 == 1:
        numbers.pop(idx)
print(numbers)            



# ## 或者让他从倒着执行删除  如下

# numbers = list(range(1000))
# 
# for idx in range(len(numbers)):
#     if numbers[-idx - 1] % 2 == 1:
#         numbers.pop(-idx - 1)
# 
# print(numbers)

# "然后我发现其实并不行qwq。发给ai他说是因为列表长度变了，索引还是会读串。他又加了一个变量，感觉这样也行\^^/"

numbers= list(range(1000))
length= len(numbers)
for idx in range(length):
    position= length - 1 - idx
    if numbers[position] % 2 == 1:
        numbers.pop(position)

