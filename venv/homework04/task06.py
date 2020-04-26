import itertools

def my_iter_1(start_value: int):
    return itertools.count(start_value)

def my_iter_2(loop_value: list):
    return itertools.cycle(loop_value)

