def my_func(summary=0):
    """
    The function requires a sequence of integers divided by comma.
    If users need to quit, they should input Q at the end of the string.
    :param summary: sum of previous values
    :return: None
    """
    need_to_quit = False

    input_values = input("Input integers separated by comma. To quit input Q.\n")

    if input_values and input_values.upper()[-1] == "Q":
        need_to_quit = True
        input_values = input_values[:-1]

    values = [int(i.strip()) for i in input_values.split(',') if i.strip().isdigit()]

    if values:
        summary += sum(values)
        print(summary)

    if need_to_quit:
        return
    else:
        my_func(summary)


my_func()
