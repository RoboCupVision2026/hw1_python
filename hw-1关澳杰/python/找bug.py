# if __name__ == "__main__":
#     list = list(range(1000))
#     for idx in range(len(list)):
#         if list[idx] % 2 == 1:
#             list.pop(idx)            删除；list[idx]后，列表长度变化
#改后：
if __name__ == "__main__":
    list = list(range(1000))
    list_2 = []
    for idx in list:
        if idx % 2 == 0:
            list_2.append(idx)
    print(list_2)