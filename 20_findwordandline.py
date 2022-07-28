content = True
i = 1
with open('poem.txt') as f:
    while content:
        content = f.readline()
        if 'moon' in content.lower():
            print(content)
            print(f'yes moon is present in {i}')
        i += 1