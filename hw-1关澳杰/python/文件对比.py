
with open("data/test.txt", "r",encoding="utf-8") as f1,open("data/copy_test.txt","r",encoding="utf-8") as f2:
    line_number = 1
    for line1,line2 in zip(f1,f2):
        if line1.strip() != line2.strip():
            print(line_number)
        line_number += 1