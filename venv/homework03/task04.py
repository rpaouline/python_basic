def my_func(x: float, y: int) -> float:
    """
    The function calculates a result of an expression x**y
    :param x: positive float
    :param y: negative int
    :return: x**y
    """

    result = 1
    i = 0
    while i < -y:
        result /= x
        i += 1

    return result
