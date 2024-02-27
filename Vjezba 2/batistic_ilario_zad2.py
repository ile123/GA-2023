def function_2(interval_1, interval_2):
    a, b = interval_1
    c, d = interval_2
    if b < c or d < a:
        print("ERROR: Something wrong with the intervals!")
        return []
    result_1 = max(a, c)
    result_2 = min(b, d)
    return [result_1, result_2]