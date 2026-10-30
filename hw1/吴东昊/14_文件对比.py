from pathlib import Path
p=Path(__file__).resolve().parent
with (p/"test.txt").open(encoding="utf-8") as f,(p/"copy_test.txt").open(encoding="utf-8") as g:
    a=f.readlines()
    b=g.readlines()
for i in range(max(len(a),len(b))):
    if i>=len(a) or i>=len(b) or a[i]!=b[i]:
        print(i+1)
