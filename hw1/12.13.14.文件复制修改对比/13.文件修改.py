from pathlib import Path
targetFile=Path(__file__).parent/"test.txt"
oldContent=targetFile.read_text(encoding="utf-8")
newContent="python"+oldContent+"python"
targetFile.write_text(newContent,encoding="utf-8")