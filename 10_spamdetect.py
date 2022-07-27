text = input("enter your text here: ")

if ("make a lot of money") in text:
    spam = True
elif("subscribe this channel") in text:
    spam = True
elif ("click this") in text:
    spam = True
elif ("buy now") in text:
    spam = True
else:
    spam = False

if(spam):
    print("this is spam")
else:
    print("this is not spam")