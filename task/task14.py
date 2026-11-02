#文件对比
with open("test.txt","r",encoding="utf-8") as f1,open("copy_test.txt","r",encoding="utf-8") as f2:
    test_content = f1.readlines()
    copy_test_content = f2.readlines()
    max_lines = max(len(test_content),len(copy_test_content))
    min_lines = min(len(test_content),len(copy_test_content))
    different_lines_list = []
    for index in range(max_lines):
        if index < min_lines:
            if test_content[index].strip() != copy_test_content[index].strip():
                different_lines_list.append(index+1)
        else:
            different_lines_list.append(index + 1)
print(different_lines_list)


