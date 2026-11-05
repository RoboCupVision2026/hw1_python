# ##  十三

with open("test.txt","r",encoding="utf-8")as file: 
    n= "python"+ file.read()+"python"
with open("test.txt", "w", encoding="utf-8") as file:
    file.write(n)
print("改好了")

