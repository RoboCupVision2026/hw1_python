import os
cr_dir = os.path.dirname(os.path.abspath(__file__))
text_dir = os.path.join(cr_dir, "text.txt")
text_copy_dir = os.path.join(cr_dir, "text_copy.txt")
with open(text_dir, "r") as f:
    l_1 = f.readlines()
    with open(text_copy_dir, "r") as f1:
        l_2 = f1.readlines()
        for i in range(min(len(l_1),len(l_2))):
            if not l_1[i]==l_2[i]:
                print(f"Line {i+1} is different.")
        if len(l_1)>len(l_2):
            for i in range(len(l_2),len(l_1)):
                print(f"Line {i+1} is different.")
        else:
            for i in range(len(l_1),len(l_2)):
                print(f"Line {i+1} is different.")