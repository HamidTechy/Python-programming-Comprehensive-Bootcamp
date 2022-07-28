import os
oldname = 'copy2.txt'
newname = 'rename_by_python'
with open(oldname) as f:
    content = f.read()

with open(newname, 'w') as f:
    f.write(content)
os.remove(oldname)