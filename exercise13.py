import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
file_path="test.txt"
with open(file_path, "r", encoding="utf-8") as f:
    note=f.read()
note2=note.rstrip('\n')
new_note="python " + note2 + " python"
with open(file_path, "w", encoding="utf-8") as f:
    f.write(new_note)