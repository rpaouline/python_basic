# variant 1
def my_func_1(a: float, b: float, c: float) -> float:
    return a + b + c - min(a, b, c)


# variant 2
def my_func_2(a: float, b: float, c: float) -> float:
    result = a + b
    if result < a + c:
        result = a + c
    if result < b + c:
        result = b + c

    return result
