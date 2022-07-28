
with open('poem.txt') as f:
    content = f.read().lower()

if 'twinkle' in content:
    print("yes twinkle is present")
else:
    print("no twinkle is not present")