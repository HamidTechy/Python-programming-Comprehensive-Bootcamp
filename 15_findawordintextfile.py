f = open("poem.txt")
t = f.read()
if 'twinkle' in t:
    print("twinke is present")
else:
    print("twinkle is not present")