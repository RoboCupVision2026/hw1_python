from pathlib import Path
p=Path(__file__).resolve().parent/"test.txt"
with p.open("r+",encoding="utf-8") as f:
    s=f.read()
    f.seek(0)
    f.write("python"+s+"python")
