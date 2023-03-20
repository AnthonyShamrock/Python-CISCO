#Python 3.1.2.10
while True:
    user_word = input("Enter word to remove vowels\n")

    found = False
    for letter in user_word:
        if letter.upper() in ["A", "E", "I", "O", "U"]:
            continue
        found = True
        print(letter)

    if not found:
        print("Only vowels were provided")

