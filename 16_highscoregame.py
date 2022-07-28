def game():
    return 56

score = game()
with open('hiscore.text') as f:
    highscore = int(f.read())

if highscore<score:
    with open('hiscore.text', 'w') as f:
        f.write(str(score))
elif highscore>score:
    with open('hiscore.text', 'w') as f:
        f.write(str(score))