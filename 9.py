from pathlib import Path
img_dir = Path("img")
img_dir.mkdir(exist_ok=True)
for i in range(100):
    file_path = img_dir / f"pic_{i:03d}.png"
    file_path.touch(exist_ok=False)
print("img資料夾以及100個png檔已建立")