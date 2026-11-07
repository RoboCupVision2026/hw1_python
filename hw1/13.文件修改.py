from pathlib import Path

path=Path(__file__).resolve().parent/"test.txt"
with open(path,"r+") as f:
    content=f.read()
    f.seek(0)
    f.write("python"+content)
    f.seek(0,2)
    f.write("python")