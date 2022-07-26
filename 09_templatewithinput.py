letter = "hi <|NAME|> this is abc company and we wish your congratulation for your selection " \
         "contact our office as soon as possible\n" \
         "<|DATE|> "
name = input(f"Enter your Name")
date = input("Enter date")
letter = letter.replace("<|NAME|>", name)
letter = letter.replace("<|DATE|>", date)
print(letter)