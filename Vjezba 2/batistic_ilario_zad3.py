def is_vowel(character):
    if 'a' == character.lower():
        return True
    elif 'e' == character.lower():
        return True
    elif 'i' == character.lower():
        return True
    elif 'o' == character.lower():
        return True
    elif 'u' == character.lower():
        return True
    else:
        return False
    

def function_3(string):
    counter = 0
    for i, character in enumerate(string):
        if is_vowel(character) and len(string) != (i + 1) and is_vowel(string[i + 1]):
            counter += 1

    return counter