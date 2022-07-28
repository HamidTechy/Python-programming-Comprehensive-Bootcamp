words = ['donkey', 'bc', 'mc']
with open("poem.txt") as f:
    sencered = f.read()

for word in words:
    sencered = sencered.replace(word, '&^%$#@')
    with open("poem.txt", 'w') as f:
        f.write(sencered)

