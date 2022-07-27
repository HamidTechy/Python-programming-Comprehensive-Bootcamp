myDict = {
    "door": "darwaza",
    "window": "khirki",
    "basket": "kore daan",
    "box": "trunk",
    "fan": "pankha"

}
print("here is the option of the word", myDict.keys())
translation = input("enter the word of english\t")
print(myDict.get(translation))
