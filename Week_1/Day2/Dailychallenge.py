def map_letters(word):
    letter_positions = {}

    for index, letter in enumerate(word):
        if letter in letter_positions:
            letter_positions[letter].append(index)
        else:
            letter_positions[letter] = [index]

    return letter_positions


user_word = input("Enter a word: ").strip().lower()


result = map_letters(user_word)
print(result)

