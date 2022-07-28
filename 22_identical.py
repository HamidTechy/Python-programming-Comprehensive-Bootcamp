
with open('this.txt') as f:
    f1 = f.read()
with open('copy.txt') as f:
    f2 = f.read()
if f1 == f2:
    print("file are identical")
else:
    print("files are not identical")