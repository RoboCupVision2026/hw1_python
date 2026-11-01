import random

if __name__ == '__main__':
    with open("data.txt",'w',encoding="utf-8") as f:
        for i in range(100000):
            num = random.randint(1,100)
            f.write(str(num)+"\n")