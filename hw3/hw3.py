"""
Create required phrase.
----------------------

You are given a string of available characters and a string representing a word or a phrase that you need to generate.
Write a function that checks if you can generate required word/phrase using the characters provided.
If you can, then please return True, otherwise return False.

NOTES:
    You can only generate the phrase if the frequency of unique characters in the characters string is equal or greater
    than frequency in the document string.

FOR EXAMPLE:

    characters = "cbacba"
    phrase = "aabbccc"

    In this case you CANNOT create required phrase, because you are 1 character short!

IMPORTANT:
    The phrase you need to create can contain any characters including special characters, capital letter, numbers
    and spaces.

    You can always generate an empty string.

"""

from collections import Counter


def generate_phrase(characters, phrase):

    char_counter = Counter(characters)
    phrase_counter = Counter(phrase)

    if not phrase_counter and not char_counter:  # if both are empty --> True
        return True

    if len(phrase) > len(characters):  # not enough characters --> False
        return False

    for character, counter in phrase_counter.items():  # make phrase_counter a list

        if character not in char_counter or counter > char_counter.get(character):
            # if character is not included in its dictionary (after Counter transformation)
            # and its count is greater than its count in the dictionary (after Counter transformation)
            return False
        else:
            return True

    return True


valid_phrase1 = generate_phrase('aabbcc', 'cabacb')  # exact same amount
valid_phrase2 = generate_phrase('gciMaai!231', 'Magic123!')  # extra characters
invalid_phrase1 = generate_phrase('CF', 'CFG')  # less characters
invalid_phrase2 = generate_phrase('&8+qdjgfhbv134?', 'Nanodegree')

print(valid_phrase1)
print(valid_phrase2)
print(invalid_phrase1)
print(invalid_phrase2)
