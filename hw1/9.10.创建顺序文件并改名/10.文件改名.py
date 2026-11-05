from pathlib import Path
import random 
imgPath=Path(__file__).parent/"img"
print(imgPath)
pngFiles=list(imgPath.glob("*.png"))
if len(pngFiles)<50:
    print("/img文件夹中.png文件不足50个！")
else:
    targetFiles=random.sample(pngFiles,50)
    for old in targetFiles:
        new=old.with_suffix(".jpg")
        old.rename(new)
    print("已成功将50个.png文件修改为.jpg")