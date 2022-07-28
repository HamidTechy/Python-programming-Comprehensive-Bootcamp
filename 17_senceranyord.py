
with open("poem.txt") as f:
    sencerd = f.read()

sencerd = sencerd.replace('donkey', '#@#$#&#')

with open("poem.txt", 'w') as f:
    f.write(sencerd)