def uplow(word):
    new_word = ''
    last_letter_small = True
    for letter in word:
        if letter == ' ':
            last_letter_small = False
        if last_letter_small:
            letter = letter.upper()
        else:
            letter = letter.lower()
        last_letter_small = not last_letter_small
        new_word = new_word + letter
    return new_word