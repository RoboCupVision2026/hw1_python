from pathlib import Path
import random
img_dir = Path("img")
png_files = list(img_dir.glob("*.png"))
selected = random.sample(png_files, 50)
for old_file in selected:
    new_file = old_file.with_suffix(".jpg")
    old_file.rename(new_file)
print("50個檔案已改成jpg")