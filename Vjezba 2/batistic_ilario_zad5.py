def function_5(array, i=0, biggest=None):
    if i == (len(array) - 1):
        return biggest
    if biggest is None:
        if type(array[i]) is int:
            biggest = array[i]
    if type(array[i]) is int and biggest < array[i]:
        biggest = array[i]
    return function_5(array, i + 1, biggest)