def my_gen(bound):
    result = 1
    for i in range(1, bound+1):
        result *= i
        yield result

