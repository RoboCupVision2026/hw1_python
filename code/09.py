# ## 第九题

from pathlib import Path
folder= Path.cwd() / "img"
folder.mkdir(exist_ok=True)
for number in range(1,101):
    file_path= folder / f"{number}.png"
    file_path.touch()
print("好了")


