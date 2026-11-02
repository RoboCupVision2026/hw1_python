#文件修改
with open("test.txt","r+",encoding="utf-8") as f:
    org_content="".join(f.readlines())
    f.seek(0)
    f.write("python\n")
    f.write(org_content)
    f.write("python\n")
    f.truncate()

