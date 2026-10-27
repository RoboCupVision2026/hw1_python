import random
file_path = "D:/项目/robocup_train_1/3_3/data.txt"
with open(file_path, "w") as f:
    for i in range(100000):
        f.write(str(random.randint(1,100))+"\n")