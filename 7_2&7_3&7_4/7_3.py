import os
cr_dir = os.path.dirname(os.path.abspath(__file__))
text_dir = os.path.join(cr_dir, "text.txt")
with open(text_dir, "r+") as f:
    old_content = f.read()
    f.seek(0)
    f.write("python" + old_content)
    f.seek(0,2)
    f.write("python")