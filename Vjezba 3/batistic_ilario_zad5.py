def function_5(dictionary):
    new_inverted = {}
    for key, values in dictionary.items():
        for value in values:
            if value not in new_inverted:
                new_inverted[value] = [key]
            else:
                new_inverted[value].append(key)
    return new_inverted
