from pathlib import Path

path=Path(__file__).resolve().parent
lines1=(path/"test.txt").read_text().splitlines()
lines2=(path/"copy_test.txt").read_text().splitlines()
l=max(len(lines1),len(lines2))
ll=min(len(lines1),len(lines2))
for i in range(ll):
    if lines1[i]!=lines2[i]:
        print(i+1)
for i in range(ll,l):
    print(i+1)